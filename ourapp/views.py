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
from .forms import ParentFeedbackForm

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
    form=TeengerFeedbackForm()
    if request.method == 'POST':
        user = request.POST.get('Teenger')
        instance = User.objects.get(username=user)
        if instance:
            form = TeengerFeedbackForm(request.POST)
            if form.is_valid():
                form.instance.Teengers = instance
                form.save()
                return redirect('feedback_psy_teenger')
    context = {'form': form}
    return render(request, 'ourapp/feedback_teenger.html', context)




def add_parent_feedback(request):
    form=ParentFeedbackForm()
    if request.method == 'POST':
        user = request.POST.get('parent')
        instance = User.objects.get(username=user)
        if instance:
            form = ParentFeedbackForm(request.POST)
            if form.is_valid():
                form.instance.Parents = instance
                form.save()
                return redirect('feedback_psy_parent')

    context = {'form': form}
    return render(request, 'ourapp/feedback_parent.html', context)


def send_sammary_to_parent(request):
    return render(request,'ourapp/send_sammary_to_parent.html')


def send_sammary_to_teen(request):
    return render(request,'ourapp/send_sammary_to_teen.html')




def add_send_sammary_to_parent(request):
    form = ParentFeedbackForm()
    if request.method == 'POST':
        user = request.POST.get('parent')
        instance = User.objects.get(username=user)
        if instance:
            form = ParentFeedbackForm(request.POST)
            if form.is_valid():
                form.instance.Parents = instance
                form.save()
                return redirect('sammaryforparent',user)

    context = {'form': form}
    return render(request, 'ourapp/send_sammary_to_parent.html', context)






def add_send_sammary_to_teen(request):

    form = TeengerFeedbackForm()
    if request.method == 'POST':
        user = request.POST.get('Teenger')
        instance = User.objects.get(username=user)
        if instance:
            form = TeengerFeedbackForm(request.POST)
            if form.is_valid():
                form.instance.Teengers = instance
                form.save()
                return redirect('sammaryforteenger')

    context = {'form': form}
    return render(request, 'ourapp/send_sammary_to_teen.html', context)


def list_of_teenger(request):
    return render(request, 'ourapp/list_of_teenger.html')



def view_list_of_teenger(request):

    users_in_group = Group.objects.get(name='Teengers').user_set.all()
    # Teengers =Teengers.objects.all()
    teen = {'users_in_group': users_in_group}
    return render(request, 'ourapp/list_of_teenger.html', teen)




def view_list_of_parent(request):

    users_in_group = Group.objects.get(name='Parents').user_set.all()
    # Teengers =Teengers.objects.all()
    parent = {'users_in_group': users_in_group}
    return render(request, 'ourapp/list_of_parent.html', parent)