from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.urls import reverse
from ourapp.forms import UpdateUserForm, profileupdateform
from django.http import HttpRequest
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from ourapp.models import TeengerFeedback
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib import messages
from .models import TeengerFeedback
from .views import add_teenger_feedback
from .forms import CreatTeengerFeedbackForm
from ourapp.models import TeengerFeedback
from ourapp.views import view_list_of_teenger
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from datetime import datetime
from . import views
from ourapp.views import add_send_sammary_to_parent
from unittest.mock import patch

from .models import ParentFeedback
from .forms import updateparentsammaryForm
from django.test import Client
from django.shortcuts import get_object_or_404
from .models import Lecture
from django.conf import settings
from .views import choicelinktopic_teenager, choicelinktopic_parent


##########################################################

class TestLoginTeenager(TestCase):
    def setUp(self):
        self.url = reverse('loginTeenager')
        self.user = User.objects.create_user(username='test_user', password='test_password')
        Group.objects.create(name='Teengers').user_set.add(self.user)

    def test_login_successful(self):
        response = self.client.post(self.url, {'username': 'test_user', 'password': 'test_password'})
        self.assertRedirects(response, reverse('homepage_teenager'))

    def test_login_unsuccessful(self):
        response = self.client.post(self.url, {'username': 'incorrect_username', 'password': 'incorrect_password'})
        self.assertContains(response, 'username OR password incorrert')



#############################################
class Testsingupteenager(TestCase):
    def setUp(self):
        self.url = reverse('singupteenger')
        self.user = User.objects.create_user(username='test_user', password='test_password')

        if not Group.objects.filter(name='Teengers').exists():
            group = Group.objects.create(name='Teengers')
            group.user_set.add(self.user)
        else:
            group = Group.objects.get(name='Teengers')
            group.user_set.add(self.user)
    def test_signup_invalid_form(self):
        response = self.client.post(self.url,{'username': '', 'password1': 'test_password123', 'password2': 'test_password123'})
        self.assertContains(response, 'This field is required.')


class TestAddParentFeedbackView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='password')

    def test_get_request(self):
        response = self.client.get(reverse('feedback_parent'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CreateParentFeedbackForm)

    # def test_valid_post_request(self):
    #     url = reverse('feedback_parent')
    #     data = {'username': 'test_user', 'text': 'Test feedback', 'date': '2022-01-03'}
    #     response = self.client.post(url, data)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(ParentFeedback.objects.filter(username='test_user', text='Test feedback').exists())

        # Check if success message is sent
        self.assertRedirects(response, expected_url=reverse('feedback_parent'))
        self.assertMessageCount(response, success=1)
        self.assertMessageContains(response, 'Feedback sent successfully!')

    def test_invalid_post_request(self):
        url = reverse('feedback_parent')
        data = {'username': 'test_user', 'text': '', 'date': '2022-01-03'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Should redirect to 'error_parent'

    def test_existing_instance_post_request(self):
        ParentFeedback.objects.create(username='test_user', text='Test feedback', date='2022-01-03')
        url = reverse('feedback_parent')
        data = {'username': 'test_user', 'text': 'Test feedback', 'date': '2022-01-03'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Should redirect to 'error_parent'

    # Helper methods
    def assertMessageCount(self, response, **kwargs):
        storage = messages.get_messages(response.wsgi_request)
        for level, count in kwargs.items():
            messages_list = list(storage)
            self.assertEqual(len([m for m in messages_list if m.level_tag == level]), count)

    def assertMessageContains(self, response, message_text):
        storage = messages.get_messages(response.wsgi_request)
        self.assertIn(message_text, [m.message for m in storage])
####################################################
class TestAddSendSummaryToParent(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password')
        self.client = Client()
        self.ParentFeedback = ParentFeedback.objects.create(parent='test_user', date='2022-01-03', sammary='Initial summary')

    def test_add_send_sammary_to_parent(self):
        url = reverse('send_sammary_to_parent', kwargs={'username': 'test_user', 'date': self.ParentFeedback.date})
        response = self.client.get(url)

        # Simulate POST request
        form_data = {'sammary': 'Updated summary'}
        response = self.client.post(url, form_data)

        # Check if the form is saved successfully
        self.assertTrue(ParentFeedback.objects.filter(sammary='Updated summary').exists())

        # Check if the success message is displayed
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(messages[0].message, 'summary sent successfully!')



class test_choicelinktopic_psy(TestCase):
    def test_choicelinktopic_psy_par(self):
        response = self.client.get(reverse('choicelinktopic_psy_par'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/choicelinktopic_psy_par.html')

    def test_choicelinktopic_psy_ten(self):
        response = self.client.get(reverse('choicelinktopic_psy_ten'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/choicelinktopic_psy_ten.html')

class TestPostLinks(TestCase):
    def test_post_e_s_ten(self):
        data = {
            'link': 'https://example.com',
            'description': 'Example Lecture'
        }
        response = self.client.post(reverse('post_e_s_ten'), data)
        self.assertEqual(response.status_code, 302)
    def test_post_c_ch_ten(self):
        data = {
            'link': 'https://example.com',
            'description': 'Example Lecture'
        }
        response = self.client.post(reverse('post_c_ch_ten'), data)
        self.assertEqual(response.status_code, 302)
    def test_post_b_ch_ten(self):
        data = {
            'link': 'https://example.com',
            'description': 'Example Lecture'
        }
        response = self.client.post(reverse('post_b_ch_ten'), data)
        self.assertEqual(response.status_code, 302)

    def test_post_b_ch_par(self):
        data = {
            'link': 'https://example.com',
            'description': 'Example Lecture'
        }
        response = self.client.post(reverse('post_b_ch_par'), data)
        self.assertEqual(response.status_code, 302)

    def test_post_c_ch_par(self):
        data = {
            'link': 'https://example.com',
            'description': 'Example Lecture'
        }
        response = self.client.post(reverse('post_c_ch_par'), data)
        self.assertEqual(response.status_code, 302)

    def test_post_t_m_par(self):
        data = {
            'link': 'https://example.com',
            'description': 'Example Lecture'
        }
        response = self.client.post(reverse('post_t_m_par'), data)
        self.assertEqual(response.status_code, 302)

class Test_view_links_psy(TestCase):
    def test_view_links_psy_par(self):
        response = self.client.get(reverse('view_links_psy_par'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/view_links_psy_par.html')

    def test_view_links_psy_ten(self):
        response = self.client.get(reverse('view_links_psy_ten'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/view_links_psy_ten.html')


class test_thank_you_page(TestCase):
    def test_thank_you_page(self):
        response = self.client.get(reverse('thank_you_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/thank_you_page.html')

class test_delete_link_psy(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.client.force_login(self.user)  # Log in as a user for testing purposes

    def test_delete_link_psy_par(self):
        # Create a Lecture object to be deleted
        link = Lecture.objects.create(forWhom='Test Link', link='http://example.com')
        response = self.client.post(reverse('delete_link_psy_par', args=[link.id]))
        self.assertEqual(response.status_code, 302)  # Or 200 if you modify the code in your website

        # Check that the link doesn't exist anymore
        link_exists = Lecture.objects.filter(id=link.id).exists()
        self.assertFalse(link_exists)


    def test_delete_link_psy_ten(self):
        # Create a Lecture object to be deleted
        link = Lecture.objects.create(forWhom='Test Link', link='http://example.com')
        response = self.client.post(reverse('delete_link_psy_ten', args=[link.id]))
        self.assertEqual(response.status_code, 302)  # Or 200 if you modify the code in your website

        # Check that the link doesn't exist anymore
        link_exists = Lecture.objects.filter(id=link.id).exists()
        self.assertFalse(link_exists)


class test_behavioral_challenges_ten(TestCase):
    def setUp(self):
        self.client = Client()

class test_choicelinktopic_par(TestCase):
    def setUp(self):
        self.client = Client()








class TestAddSendSummaryToTeen(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password')
        self.client = Client()
        self.TeengerFeedback = TeengerFeedback.objects.create(Teenger='test_user', date='2022-01-03', sammary='Initial summary')

    def test_add_send_sammary_to_teen(self):
        url = reverse('send_sammary_to_teen', kwargs={'username': 'test_user', 'date': self.TeengerFeedback.date})
        response = self.client.get(url)

        # Simulate POST request
        form_data = {'sammary': 'Updated summary'}
        response = self.client.post(url, form_data)

        # Check if the form is saved successfully
        self.assertTrue(TeengerFeedback.objects.filter(sammary='Updated summary').exists())

        # Check if the success message is displayed
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(messages[0].message, 'summary sent successfully!')




class feedback_psy_teengerTestCase(TestCase):
     def test_feedback_psy_teenger(self):
         response = self.client.get(reverse('feedback_psy_teenger'))

         self.assertEqual(response.status_code, 200)

         self.assertTemplateUsed(response, 'ourapp/feedback_psy_teenger.html')




class feedback_psy_parentTestCase(TestCase):
    def test_feedback_psy_parent(self):
        response = self.client.get(reverse('feedback_psy_parent'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'ourapp/feedback_psy_parent.html')