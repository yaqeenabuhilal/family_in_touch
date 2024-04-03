from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Parents(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=200,null=True)
    data_created=models.DateTimeField(auto_now_add=True)
    emailsdfgh = models.CharField(max_length=200,null=True)

class Teengers(models.Model):
    name=models.CharField(max_length=200,null=False)
    phone=models.CharField(max_length=10,null=False)
    email = models.CharField(max_length=200, null=False)
class Psychotherapist(models.Model):
    name=models.CharField(max_length=200,null=False)
    phone=models.CharField(max_length=10,null=False)
    email = models.CharField(max_length=200, null=False)
class Lecture(models.Model):
    link=models.CharField(max_length=200,null=False)
    forWhom=models.CharField(max_length=200,null=False)
    Description=models.CharField(max_length=200,null=False)
class ParentFeedback(models.Model):
    parent=models.CharField(max_length=200,null=True)
    text=models.CharField(max_length=200,null=True)
class TeengerFeedback(models.Model):
    Teenger=models.CharField(max_length=200,null=True)
    text=models.CharField(max_length=200,null=True)
class profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}profile'

