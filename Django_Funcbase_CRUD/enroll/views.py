from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from . models import Student
# # Create your views here.

# # This Function Will Add new Item and Show All Items
def add_show(request):
  # return render(request, 'enroll/addandshow.html')
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
   nm = fm.cleaned_data['name']
   em = fm.cleaned_data['email']
   pw = fm.cleaned_data['address']
   p1 = fm.cleaned_data['contact']
   reg = Student(name=nm, email=em, address=pw, contact=p1)
   reg.save()
   fm = StudentRegistration()
 else:
  fm = StudentRegistration()
 #return render(request, 'enroll/addandshow.html', {'form':fm}) 
 stud = Student.objects.all()
 return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This Function will Update/Edit
def update_data(request, id):
 if request.method == 'POST':
  pi = Student.objects.get(pk=id)
  fm = StudentRegistration(request.POST, instance=pi)
  if fm.is_valid():
   fm.save()
 else:
  pi = Student.objects.get(pk=id)
  fm = StudentRegistration(instance=pi)
 return render(request, 'enroll/updatestudent.html', {'form':fm})

# This Function will Delete
def delete_data(request, id):
 if request.method == 'POST':
  pi = Student.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')