from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from .models import TeengerFeedback
from .models import ParentFeedback

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']


class TeengerFeedbackForm(ModelForm):
    class Meta:
        model = TeengerFeedback
        fields =['Teenger','text','sammary']




class ParentFeedbackForm(ModelForm):
    class Meta:
        model = ParentFeedback
        fields =['parent','text','sammary']
