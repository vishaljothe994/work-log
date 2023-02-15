from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.urls import reverse
from django.views.generic import View

# Create your views here.
def index(request):
    return render(request, 'index.html')

def load_data(request):
    object_list = Post.objects.all()
    json = serializers.serialize('json', object_list)
    return HttpResponse(json, content_type='application/json')



class PostStore(View):
    form_class = PostForm
    template_name = 'index.html'

    def post(self, request):
        form = self.form_class(request.POST)
        #data = {'error': form.errors}
        if form.is_valid():
            try:
                title = request.POST.get('title')
                description = request.POST.get('description')
                remark = request.POST.get('remark')

                obj = get_object_or_404(Post, id=request.POST.get('post_id'))
                obj.title=title
                obj.description=description
                obj.remark=remark
                obj.save()
                return JsonResponse({'success': True, 'message': 'Post Updated Successfully!'})
            except:
                obj = Post(title=request.POST.get('title'),description=request.POST.get('description'),remark=request.POST.get('remark')) #add more fields
                obj.save()
                return JsonResponse({'success': True, 'message': 'Post Created Successfully!'})
        else:
            return JsonResponse({'error': True, 'error': form.errors})
        return render(request, self.template_name,{'data':data})




def post_edit(request,id):
    if request.method == 'GET':

        posts = Post.objects.filter(id=id).first()

        return JsonResponse({'id':posts.id,'title':posts.title,'description':posts.description,'remark':posts.remark})
    else:
        return JsonResponse({'errors':'Something went wrong!'})



def post_delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))
   