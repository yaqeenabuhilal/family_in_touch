from django.shortcuts import render, redirect,get_object_or_404
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
# views.py
from django.shortcuts import render
from .models import Lecture



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



def choicelinktopic_teenager(request):
    return render(request, 'ourapp/choicelinktopic_teenager.html')

def behavioral_challenges_ten(request):
    links = Lecture.objects.filter(forWhom="Behavioral Challenges For Teenagers")
    return render(request, 'ourapp/behavioral_challenges_ten.html', {'behavioral_challenges_ten': links})


def communication_challenges_ten(request):
    links = Lecture.objects.filter(forWhom="Communication Challenges For Teenagers")
    return render(request, 'ourapp/communication_challenges_ten.html', {'communication_challenges_ten': links})

def emotional_support_ten(request):
    links = Lecture.objects.filter(forWhom="Emotional Support")
    return render(request, 'ourapp/emotional_support_ten.html', {'emotional_support_ten': links})

def choicelinktopic_parent(request):
    return render(request, 'ourapp/choicelinktopic_parent.html')

def behavioral_challenges_par(request):
    links = Lecture.objects.filter(forWhom="Behavioral Challenges For Parents")
    return render(request, 'ourapp/behavioral_challenges_par.html', {'behavioral_challenges_par': links})

def communication_challenges_par(request):
    links = Lecture.objects.filter(forWhom="Communication Challenges For Parents")
    return render(request, 'ourapp/communication_challenges_par.html', {'communication_challenges_par': links})


def time_management_par(request):
    links = Lecture.objects.filter(forWhom="Time Management")
    return render(request, 'ourapp/time_management_par.html', {'time_management_par': links})

def choicelinktopic_psy_par(request):
    return render(request, 'ourapp/choicelinktopic_psy_par.html')
def choicelinktopic_psy_ten(request):
    return render(request, 'ourapp/choicelinktopic_psy_ten.html')



def post_e_s_ten(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        description = request.POST.get('description')
        if link and description:
            Lecture.objects.create(link=link, Description=description, forWhom="Emotional Support")
            # פעולות נוספות אם יש צורך...
            return redirect('thank_you_page')  # Assuming 'thank_you_page' is the name of your URL pattern for the Thank You page
        else:
            return render(request, 'ourapp/post_e_s_ten.html', {'error_message': 'Invalid form data'})
    else:
        return render(request, 'ourapp/post_e_s_ten.html')

def post_c_ch_ten(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        description = request.POST.get('description')
        if link and description:
            Lecture.objects.create(link=link, Description=description, forWhom="Communication Challenges For Teenagers")
            # פעולות נוספות אם יש צורך...
            return redirect('thank_you_page')  # Assuming 'thank_you_page' is the name of your URL pattern for the Thank You page
        else:
            return render(request, 'ourapp/communication_challenges_ten.html', {'error_message': 'Invalid form data'})

    else:
        return render(request, 'ourapp/post_c_ch_ten.html')


def post_b_ch_ten(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        description = request.POST.get('description')
        if link and description:
            Lecture.objects.create(link=link, Description=description, forWhom="Behavioral Challenges For Teenagers")
            # פעולות נוספות אם יש צורך...
            return redirect('thank_you_page')  # Assuming 'thank_you_page' is the name of your URL pattern for the Thank You page
        else:
            return render(request, 'ourapp/post_b_ch_ten.html', {'error_message': 'Invalid form data'})
    else:
        return render(request, 'ourapp/post_b_ch_ten.html')




def post_t_m_par(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        description = request.POST.get('description')
        if link and description:
            Lecture.objects.create(link=link, Description=description, forWhom="Time Management")
            # Redirect to the Thank You page after successful submission
            return redirect('thank_you_page')  # Assuming 'thank_you_page' is the name of your URL pattern for the Thank You page
        else:
            return render(request, 'ourapp/post_t_m_par.html', {'error_message': 'Invalid form data'})
    else:
        return render(request, 'ourapp/post_t_m_par.html')

def post_c_ch_par(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        description = request.POST.get('description')
        if link and description:
            Lecture.objects.create(link=link, Description=description, forWhom="Communication Challenges For Parents")
            # פעולות נוספות אם יש צורך...
            return redirect('thank_you_page')  # Assuming 'thank_you_page' is the name of your URL pattern for the Thank You page
        else:
            return render(request, 'ourapp/post_c_ch_par.html', {'error_message': 'Invalid form data'})
    else:
        return render(request, 'ourapp/post_c_ch_par.html')

def post_b_ch_par(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        description = request.POST.get('description')
        if link and description:
            Lecture.objects.create(link=link, Description=description, forWhom="Behavioral Challenges For Parents")
            # Additional actions if needed...
            return redirect('thank_you_page')  # Assuming 'thank_you_page' is the name of your URL pattern for the Thank You page
        else:
            return render(request, 'ourapp/post_b_ch_par.html', {'error_message': 'Invalid form data'})
    else:
        return render(request, 'ourapp/post_b_ch_par.html')






def view_links_psy_par(request):
    links = Lecture.objects.all()  # Get all links uploaded by the psychologist
    return render(request, 'ourapp/view_links_psy_par.html', {'links': links})

def delete_link_psy_par(request, link_id):
    link = get_object_or_404(Lecture, pk=link_id)  # Retrieve the link object or return 404 if not found
    if request.method == 'POST':
        # Delete the link
        link.delete()
        # Redirect to the psychologist links management page after deletion
        return redirect('view_links_psy_par')
    else:
        # Render a confirmation page if the request method is not POST
        return render(request, 'delete_link_psy_par.html', {'link': link})


def view_links_psy_ten(request):
    links = Lecture.objects.all()  # Get all links uploaded by the psychologist
    return render(request, 'ourapp/view_links_psy_ten.html', {'links': links})

def delete_link_psy_ten(request, link_id):
    link = get_object_or_404(Lecture, pk=link_id)  # Retrieve the link object or return 404 if not found
    if request.method == 'POST':
        # Delete the link
        link.delete()
        # Redirect to the psychologist links management page after deletion
        return redirect('view_links_psy_ten')
    else:
        # Render a confirmation page if the request method is not POST
        return render(request, 'delete_link_psy_ten.html', {'link': link})


def thank_you_page(request):
    return render(request, 'ourapp/thank_you_page.html')



