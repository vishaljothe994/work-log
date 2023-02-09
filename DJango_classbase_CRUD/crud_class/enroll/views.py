from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from . models import Student
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
# # Create your views here.


# This Class Will Add new Item and Show All Items
class UserAddShowView(TemplateView):
  template_name = 'enroll/addandshow.html'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    fm = StudentRegistration()
    stud = Student.objects.all()
    context = {'stu':stud, 'form':fm}
    return context
  
  def post(self, request):
    fm = StudentRegistration(request.POST)
    if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      pw = fm.cleaned_data['address']
      p1 = fm.cleaned_data['contact']
      reg = Student(name=nm, email=em, address=pw, contact=p1)
      reg.save()
    return HttpResponseRedirect('/')






# # This Function will Update/Edit
# def update_data(request, id):
#  if request.method == 'POST':
#   pi = Student.objects.get(pk=id)
#   fm = StudentRegistration(request.POST, instance=pi)
#   if fm.is_valid():
#    fm.save()
#  else:
#   pi = Student.objects.get(pk=id)
#   fm = StudentRegistration(instance=pi)
#  return render(request, 'enroll/updatestudent.html', {'form':fm})



# This Class will Update/Edit
class UserUpdateView(View):
  def get(self, request, id):
    pi = Student.objects.get(pk=id)
    fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})
  
  def post(self, request, id):
    pi = Student.objects.get(pk=id)
    fm = StudentRegistration(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
    return render(request, 'enroll/updatestudent.html', {'form':fm})




# # This Function will Delete
# def delete_data(request, id):
#  if request.method == 'POST':
#   pi = Student.objects.get(pk=id)
#   pi.delete()
#   return HttpResponseRedirect('/')




# This Class will Delete
class UserDeleteView(RedirectView):
  url = '/'
  def get_redirect_url(self, *args, **kwargs):
    del_id = kwargs['id']
    Student.objects.get(pk=del_id).delete()
    return super().get_redirect_url(*args, **kwargs)