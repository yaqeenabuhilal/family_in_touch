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
from .forms import CreateUserForm,profileupdateform, UpdateUserForm
from django.contrib.auth.models import User
from .models import profile
from ourapp.models import profile
from django.shortcuts import reverse
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
#####
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render



def home(request):
    return render(request,'ourapp/dashbord.html')

def feedback(request):
    return render(request,'ourapp/feedback.html')
def link(request):
    return render(request,'ourapp/link.html')
def loginTeenager(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Teengers').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('homepage_teenager')
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
                return redirect('homepage_parent')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request,'ourapp/log _in _parent.html',context)
def login_psy(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Psychotherapist').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('homepageforpsy')

            else:
                messages.info(request, 'username OR password incorrert')
        else:
                messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'ourapp/login_psy.html', context)

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

def navbarforpsy(request):
    return render(request, 'ourapp/navbarforpsy.html')
def homepageforpsy(request):
    return render(request, 'ourapp/homepageforpsy.html')
def homepage_parent(request):
    return render(request, 'ourapp/homepage_parent.html')
def homepage_teenager(request):
    return render(request, 'ourapp/homepage_teenager.html')
def profile(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST,instance=request.user)
        p_form = profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = profileupdateform(instance=request.user.profile)
    context = {'u_form':u_form,'p_form':p_form}
    return render(request, 'ourapp/profile.html', context)

def my_view(request):
    user = request.user
    groups = user.groups.all()
    return render(request, 'ourapp/profile.html', {'user_groups': groups})

