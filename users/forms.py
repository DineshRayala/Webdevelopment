from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    phone= forms.CharField(max_length=10,required=True)
    hod_id = forms.CharField(max_length=30, required=True)
    designation = forms.CharField(max_length=30, required=True)
    department_number= forms.CharField(required=True)
    address = forms.CharField(max_length=200, required=True)
  

    class Meta:
        model=User
        fields=['hod_id','password1','password2','username','department_number','designation','email','phone','address']