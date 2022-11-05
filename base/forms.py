from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm



class MyUserCreationform(UserCreationForm):
     class Meta:
        model = User
        fields = ['name', 'username', 'email','password1', 'password2']
class Roomform(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class Userform(ModelForm):
    class Meta:
         model= User
         fields = ['avatar','name', 'username', 'email','bio']