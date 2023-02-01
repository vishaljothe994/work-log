# from django.core import validators
from django import forms
from enroll.models import Student

class StudentRegistration(forms.ModelForm):
 class Meta:
  model = Student
  fields = ['name', 'email', 'address','contact']
  # widgets = {
  #  'name': forms.TextInput(attrs={'class':'form-control'}),
  #  'email': forms.EmailInput(attrs={'class':'form-control'}),
  #  'address': forms.TextInput(attrs={'class':'form-control'}),
  #  'contact': forms.IntegerField(attrs={'class':'form-control'}),
  # }