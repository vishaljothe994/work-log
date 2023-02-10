from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from .models import Member
 
# Create your views here.
def index(request):
    all_members = Member.objects.all()
    return render(request, 'datatables/index.html', {'all_members': all_members})
 
def insert(request):
  if request.method == "POST":  
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'], address=request.POST['address'])
    member.save()
    data1 = Member.objects.values()
    student_data = list(data1)
    return JsonResponse({'status':'Save', 'student_data':student_data})
    #ser_instance = serializers.serialize('json', [ data1, ])
    #return JsonResponse({"instance": ser_instance}, status='Save')
    #return JsonResponse({'status':'Save', 'instance':ser_instance})
    #return redirect('/')
    #return JsonResponse({'status':1,'member':data1})

  else:
    return JsonResponse({'status':0})