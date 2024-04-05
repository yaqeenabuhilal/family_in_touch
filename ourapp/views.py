from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from itertools import count, repeat, chain
from .forms import CreateUserForm, profileupdateform, UpdateUserForm
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

from itertools import count, repeat, chain
from .forms import CreateUserForm
# views.py
from django.shortcuts import render
from .models import Lecture

from .forms import TeengerFeedbackForm
from .forms import ParentFeedbackForm, updateTeengersammaryForm, updateparentsammaryForm
from .forms import CreateParentFeedbackForm
from .forms import CreatTeengerFeedbackForm
from datetime import datetime




# def home(request):
#     return render(request, 'ourapp/dashbord.html')
#
# def feedback_parent(request):
#     return render(request,'ourapp/feedback_parent.html')
#
#
# def feedback_teenger(request):
#     return render(request,'ourapp/feedback_teenger.html')

def feedback_psy_teenger(request):
    feedback_psy_teenger=TeengerFeedback.objects.all()

    return render(request,'ourapp/feedback_psy_teenger.html',{'feedback_psy_teenger':feedback_psy_teenger})
def feedback_psy_parent(request):
    feedback_psy_parent=ParentFeedback.objects.all()

    return render(request,'ourapp/feedback_psy_parent.html',{'feedback_psy_parent':feedback_psy_parent})
# def summary_psy(request):
#     return render(request,'ourapp/summary_psy.html')
#
#
# def drop_down_list_psy(request):
#     return render(request,'ourapp/drop_down_list_psy.html')


# def feedback(request):
#     return render(request, 'ourapp/feedback.html')
#
#
# def link(request):
#     return render(request, 'ourapp/link.html')
#
#
#     return render(request,'ourapp/link.html')
# def testerforfeed(request):
#     return render(request,'ourapp/testerforfeed.html')
#




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



# def test(request):
#     return render(request, 'ourapp/test.html')
#
#
# def aaa(request):
#     return render(request, 'ourapp/login.html')

# def abes_contact_us(request):
#     return render(request,'ourapp/abes_contact_us.html')
#

# def test_addfeedbackteen(request):
#     return render(request,'ourapp/test_addfeedbackteen.html')

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

def profileforparent(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST,instance=request.user)
        p_form = profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profileforparent')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = profileupdateform(instance=request.user.profile)
    context = {'u_form':u_form,'p_form':p_form}
    return render(request, 'ourapp/profileforparent.html', context)

def profileforteenager(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST,instance=request.user)
        p_form = profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profileforteenager')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = profileupdateform(instance=request.user.profile)
    context = {'u_form':u_form,'p_form':p_form}
    return render(request, 'ourapp/profileforteenager.html', context)




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


# def sammaryforparent1(request, parent_id):  # Add default value None for parent_id
#     parent = get_object_or_404(User, username=parent_id)
#
#     # Fetch feedback related to the specified teenger
#     parent_feedback = ParentFeedback.objects.filter(Parents=parent)
#
#     return render(request, 'ourapp/sammaryforparent.html', {'parent_feedback': parent_feedback, 'parent': parent})
#     # user=User.objects.get(username=pk)
#     # 	order = user.order_set.all()
#     if parent_id:
#         # Get the parent object or return 404 if not found
#         parent = get_object_or_404(User, username=parent_id)
#         # Fetch feedback related to the specified parent
#         parent_feedback = ParentFeedback.objects.filter(Parent=parent)
#     else:
#         # Handle the case where parent_id is not provided
#         parent = None
#         parent_feedback = None
#     return render(request, 'ourapp/sammaryforparent.html', {'parent_feedback': parent_feedback, 'parent': parent})

def sammaryforparent(request, parent_id):
    parent = get_object_or_404(User, username=parent_id)
    parent_feedback = ParentFeedback.objects.filter(Parents=parent)
    return render(request, 'ourapp/sammaryforparent.html', {'parent_feedback': parent_feedback, 'parent': parent})


def sammaryforteenger(request, teenger_id):
    # Get the teenger object or return 404 if not found
    teenger = get_object_or_404(User, username=teenger_id)

    # Fetch feedback related to the specified teenger
    teenger_feedback = TeengerFeedback.objects.filter(Teenger=teenger)

    return render(request, 'ourapp/sammaryforteenger.html', {'teenger_feedback': teenger_feedback, 'teenger': teenger})
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
                messages.success(request, 'Feedback sent successfully!')

            else:
                return redirect('error_teenger')
        else:
            return redirect('error_teenger')
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
                messages.success(request, 'Feedback sent successfully!')
            else:
                return redirect('error_parent')
        else:
            return redirect('error_parent')
    context = {'form': form}
    return render(request, 'ourapp/feedback_parent.html', context)









# def send_sammary_to_parent(request):
#     return render(request,'ourapp/send_sammary_to_parent.html')
#
#
# def send_sammary_to_teen(request):
#     return render(request,'ourapp/send_sammary_to_teen.html')






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
                messages.success(request, 'summary sent successfully!')
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
                messages.success(request, 'summary sent successfully!')
            else:
                return redirect('sammaryforteenger', username)

    context = {'form': form}
    return render(request, 'ourapp/send_sammary_to_teen.html', context)





# def list_of_teenger(request):
#     return render(request, 'ourapp/list_of_teenger.html')



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


def navbar_parent(request):
    return render(request, 'ourapp/navbar_parent.html')


def navbar_teenager(request):
    return render(request, 'ourapp/navbar_teenager.html')


def official_homepage(request):
    return render(request, 'ourapp/official_homepage.html')


def About(request):
    return render(request, 'ourapp/About.html')


def contact_teens(request):
    return render(request, 'ourapp/contact_teens.html')


def contact_parent(request):
    return render(request, 'ourapp/contact_parent.html')


def logout_view(request):
    logout(request)
    return redirect('official_homepage')


def logout_parent(request):
    return render(request, 'ourapp/logout_parent.html')


def logout_teens(request):
    return render(request, 'ourapp/logout_teens.html')


def logout_psy(request):
    return render(request, 'ourapp/logout_psy.html')


def error_parent(request):
    return render(request, 'ourapp/error_parent.html')
def error_teenger(request):
    return render(request, 'ourapp/error_teenger.html')