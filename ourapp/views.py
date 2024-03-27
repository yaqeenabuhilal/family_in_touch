from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from itertools import count, repeat,chain
from .forms import CreateUserForm


def home(request):
    return render(request,'ourapp/dashbord.html')

def feedback_parent(request):
    return render(request,'ourapp/feedback_parent.html')


def feedback_teenger(request):
    return render(request,'ourapp/feedback_teenger.html')

def feedback_psy_teenger(request):
    feedback_psy_teenger=TeengerFeedback.objects.all()

    return render(request,'ourapp/feedback_psy_teenger.html',{'feedback_psy_teenger':feedback_psy_teenger})
def feedback_psy_parent(request):
    feedback_psy_parent=ParentFeedback.objects.all()

    return render(request,'ourapp/feedback_psy_parent.html',{'feedback_psy_parent':feedback_psy_parent})
def summary_psy(request):
    return render(request,'ourapp/summary_psy.html')


def drop_down_list_psy(request):
    return render(request,'ourapp/drop_down_list_psy.html')

def feedback(request):
    return render(request,'ourapp/feedback.html')
def link(request):
    return render(request,'ourapp/link.html')
def testerforfeed(request):
    return render(request,'ourapp/testerforfeed.html')





def loginTeenager(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Teengers').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('dashbord')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return  render(request,'ourapp/login.html',context)
def test(request):
    return render(request,'ourapp/test.html')
def aaa(request):
    return render(request,'ourapp/login.html')

def singupteenager(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Teengers')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('loginTeenager')
    context = {'form': form}
    return render(request, 'ourapp/singupteenager.html', context)
def loginParent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Parents').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('dashbord')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request,'ourapp/log _in _parent.html',context)
def loginpsychologist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Psychotherapist').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('dashbord')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'ourapp/log_in_psy.html', context)




def sign_up_parent(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Parents')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('loginParent')
    context = {'form': form}
    return render(request, 'ourapp/sign_up_parent.html', context)
