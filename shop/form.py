from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class customerUserForm(UserCreationForm):
   username=forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control','placeholder':' Enter your  username'}))
   email=forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control','placeholder':' Enter your email '}))
   password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'forms-control','placeholder':' Enter your  password' }))
   password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'forms-control','placeholder':' Enter confirm password' }))

class meta:
        model=User
        fields=['username','email','password1','password2']