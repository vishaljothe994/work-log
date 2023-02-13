from django.shortcuts import render, redirect
from app1.models import Member
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
  
def create(request):
    if request.POST.get('member_key')=='':
        print('herer no id')
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    else:
        print('hererid')
        member = Member(id=request.POST.get('member_key'),firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/')
  
def read(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'result.html', context)
  
def edit(request):
    id = request.POST.get('uid')
    print(id)
    member = Member.objects.filter(id=id)
    print(member)
    member = Member.objects.filter(id=id).first()
    data = {'firstname':member.firstname,'lastname':member.lastname,'id':member.id}
    print(data)

    context = {'member': data}
    
    return JsonResponse( context)
  
  
# def update(request, id):
#     member = Member.objects.get(id=id)
#     member.firstname = request.POST['firstname']
#     member.lastname = request.POST['lastname']
#     member.save()
#     return redirect('/')
  
  
def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/')