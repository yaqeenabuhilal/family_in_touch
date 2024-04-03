from django.shortcuts import render, redirect, get_object_or_404
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
from .forms import TeengerFeedbackForm
from .forms import ParentFeedbackForm,updateTeengersammaryForm,updateparentsammaryForm
from .forms import CreateParentFeedbackForm
from .forms import CreatTeengerFeedbackForm
from datetime import datetime




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
def abes_contact_us(request):
    return render(request,'ourapp/abes_contact_us.html')


def test_addfeedbackteen(request):
    return render(request,'ourapp/test_addfeedbackteen.html')

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
def loginpsychologist(request):
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
    return render(request, 'ourapp/loginpsychologist.html', context)

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
def sammaryforparent(request, parent_id):
    # Get the parent object or return 404 if not found
    parent = get_object_or_404(User, username=parent_id)
    # Fetch feedback related to the specified parent
    parent_feedback = ParentFeedback.objects.filter(Parents=parent)
    return render(request, 'ourapp/sammaryforparent.html', {'parent_feedback': parent_feedback, 'parent': parent})


def sammaryforteenger(request, teenger_id):
    # Get the teenger object or return 404 if not found

    teenger = User.objects.get(username=teenger_id)
    # Fetch feedback related to the specified parent
    teenger_feedback = TeengerFeedback.objects.filter(Teengers=teenger)
    return render(request, 'ourapp/sammaryforteenger.html', {'teenger_feedback':  teenger_feedback, 'teenger': teenger})

# user=User.objects.get(username=pk)
# 	order = user.order_set.all()
# 	context = {'order':order,'item':pk}
# 	return render(request, 'ourproject/review_myorder_customrt.html', context)
# def best_sales(request):


def add_teenger_feedback(request):
    form = CreatTeengerFeedbackForm()
    if request.method == 'POST':
        date = request.POST.get('date')
        instance = TeengerFeedback.objects.filter(date=date)
        if not instance:
            form = CreatTeengerFeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('feedback_psy_teenger')
            else:
                messages.info(request, 'the info is not valid')
        else:
            messages.info(request, 'this product already exsited')
    context = {'form': form}
    return render(request, 'ourapp/feedback_teenger.html', context)







def add_parent_feedback(request):
    form = CreateParentFeedbackForm()
    if request.method == 'POST':
        date = request.POST.get('date')
        instance = ParentFeedback.objects.filter(date=date)
        if not instance:
            form = CreateParentFeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('feedback_psy_parent')
            else:
                messages.info(request, 'the info is not valid')
        else:
            messages.info(request, 'this product already exsited')
    context = {'form': form}
    return render(request, 'ourapp/feedback_parent.html', context)









def send_sammary_to_parent(request):
    return render(request,'ourapp/send_sammary_to_parent.html')


def send_sammary_to_teen(request):
    return render(request,'ourapp/send_sammary_to_teen.html')






def add_send_sammary_to_parent(request,username,date):
    date_object1 = datetime.strptime(date, '%Y-%m-%d').date()

    feed1=ParentFeedback.objects.filter(date=date_object1).get(parent=username)
    form = updateparentsammaryForm(instance=feed1)
    if request.method == 'POST':

        # isnstance=TeengerFeedback.objects.get(date=date).get(Teenger=Teenger)
        if feed1:
            form = updateparentsammaryForm(request.POST,instance=feed1)
            if form.is_valid():
                form.save()
                return redirect('sammaryforparent',username)  # Redirect to a success page
    context = {'form': form}
    return render(request, 'ourapp/send_sammary_to_parent.html', context)












def add_send_sammary_to_teen(request,username,date):
    date_object = datetime.strptime(date, '%Y-%m-%d').date()

    feed=TeengerFeedback.objects.filter(date=date_object).get(Teenger=username)
    form = updateTeengersammaryForm(instance=feed)
    if request.method == 'POST':

        # isnstance=TeengerFeedback.objects.get(date=date).get(Teenger=Teenger)
        if feed:
            form = updateTeengersammaryForm(request.POST,instance=feed)
            if form.is_valid():
                form.save()
                return redirect('sammaryforteenger',username)  # Redirect to a success page
    context = {'form': form}
    return render(request, 'ourapp/send_sammary_to_teen.html', context)





def list_of_teenger(request):
    return render(request, 'ourapp/list_of_teenger.html')



def view_list_of_teenger(request):
    users_in_group = Group.objects.get(name='Teengers').user_set.all()
    # Teengers =Teengers.objects.all()
    feed=TeengerFeedback.objects.all()
    teen = {'users_in_group': users_in_group,'feed':feed}
    return render(request, 'ourapp/list_of_teenger.html', teen)




def view_list_of_parent(request):
    users_in_group1 = Group.objects.get(name='Parents').user_set.all()
    # Teengers =Teengers.objects.all()
    feed1=ParentFeedback.objects.all()
    parent = {'users_in_group1': users_in_group1,'feed1':feed1}
    return render(request, 'ourapp/list_of_parent.html', parent)

def navbarforpsy(request):
    return render(request, 'ourapp/navbarforpsy.html')
def homepageforpsy(request):
    return render(request, 'ourapp/homepageforpsy.html')
def homepage_parent(request):
    return render(request, 'ourapp/homepage_parent.html')
def homepage_teenager(request):
    return render(request, 'ourapp/homepage_teenager.html')

