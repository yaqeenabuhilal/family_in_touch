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

from .models import ParentFeedback
from .forms import updateparentsammaryForm


# class ProfileTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
#         self.client.login(username='testuser', password='testpassword')
#
#     def test_profile_view_post(self):
#         data = {'username': 'newusername', 'email': 'newemail@example.com'}
#         response = self.client.post(reverse('profile'), data)
#         self.assertEqual(response.status_code, 302)
#
#         self.user.refresh_from_db()
#         self.assertEqual(self.user.username, 'newusername')
#         self.assertEqual(self.user.email, 'newemail@example.com')
#
#     def test_profile_view_get(self):
#         response = self.client.get(reverse('profile'))
#         self.assertEqual(response.status_code, 200)
#
#         self.assertTrue('u_form' in response.context)
#         self.assertTrue('p_form' in response.context)
#         self.assertIsInstance(response.context['u_form'], UpdateUserForm)
#         self.assertIsInstance(response.context['p_form'], profileupdateform)
#
# class NavbarForPsyTestCase(TestCase):
#     def test_navbarforpsy_view(self):
#         response = self.client.get(reverse('navbarforpsy'))
#
#         self.assertEqual(response.status_code, 200)
#
#         self.assertTemplateUsed(response, 'ourapp/navbarforpsy.html')
#
# class HomepageForPsyTestCase(TestCase):
#     def test_homepageforpsy_view(self):
#         response = self.client.get(reverse('homepageforpsy'))
#
#         self.assertEqual(response.status_code, 200)
#
#         self.assertTemplateUsed(response, 'ourapp/homepageforpsy.html')
#
#
# class TestLoginParent(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.group = Group.objects.create(name='Parents')
#         self.user = User.objects.create_user(username='test_parent', password='testpassword')
#         self.group.user_set.add(self.user)
#
#     def test_login_successful(self):
#         response = self.client.post(reverse('loginParent'), {'username': 'test_parent', 'password': 'testpassword'})
#         self.assertEqual(response.status_code, 302)  # Should redirect to homepage_parent
#
#     def test_login_unsuccessful(self):
#         response = self.client.post(reverse('loginParent'), {'username': 'incorrect_username', 'password': 'incorrect_password'})
#         self.assertEqual(response.status_code, 200)  # Should stay on the login page
#         self.assertContains(response, 'username OR password incorrert')
#
#     def test_login_non_parent_user(self):
#         non_parent_user = User.objects.create_user(username='non_parent_user', password='testpassword')
#         response = self.client.post(reverse('loginParent'), {'username': 'non_parent_user', 'password': 'testpassword'})
#         self.assertEqual(response.status_code, 200)  # Should stay on the login page
#         self.assertContains(response, 'username OR password incorrert')
#
# class TestHomepageTeenager(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_homepage_teenager_view(self):
#         response = self.client.get(reverse('homepage_teenager'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'ourapp/homepage_teenager.html')
#
# class TestNavbarTeenager(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_navbar_teenager_view(self):
#         response = self.client.get(reverse('navbar_teenager'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'ourapp/navbar_teenager.html')
#
# class TestHomepageParent(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_homepage_parent_view(self):
#         response = self.client.get(reverse('homepage_parent'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'ourapp/homepage_parent.html')
#
#
###########################################################

# class TestLoginTeenager(TestCase):
#     def setUp(self):
#         self.url = reverse('loginTeenager')
#         self.user = User.objects.create_user(username='test_user', password='test_password')
#         Group.objects.create(name='Teengers').user_set.add(self.user)
#
#     def test_login_successful(self):
#         response = self.client.post(self.url, {'username': 'test_user', 'password': 'test_password'})
#         self.assertRedirects(response, reverse('homepage_teenager'))
#
#     def test_login_unsuccessful(self):
#         response = self.client.post(self.url, {'username': 'incorrect_username', 'password': 'incorrect_password'})
#         self.assertContains(response, 'username OR password incorrert')
#


##############################################
# class Testsingupteenager(TestCase):
#     def setUp(self):
#         self.url = reverse('singupteenger')
#         self.user = User.objects.create_user(username='test_user', password='test_password')
#
#         if not Group.objects.filter(name='Teengers').exists():
#             group = Group.objects.create(name='Teengers')
#             group.user_set.add(self.user)
#         else:
#             group = Group.objects.get(name='Teengers')
#             group.user_set.add(self.user)
#     def test_signup_invalid_form(self):
#         response = self.client.post(self.url,{'username': '', 'password1': 'test_password123', 'password2': 'test_password123'})
#         self.assertContains(response, 'This field is required.')
#
########################################################################3
# class TestSummaryForTeengerView(TestCase):
#     def setUp(self):
#         # Create a test user (teenger)
#         self.teenger = User.objects.create(username='test_teenger')
#         # Create some teenger feedback
#         self.feedback1 = TeengerFeedback.objects.create(Teengers=self.teenger, text="Test Feedback 1",date="2022-03-01",sammary="ff")
#         self.feedback2 = TeengerFeedback.objects.create(Teengers=self.teenger, text="Test Feedback 2",date="2022-04-01",sammary="ff")
#
#     def test_summary_for_teenger_view(self):
#         # URL for the summary for teenger view
#         url = reverse('sammaryforteenger', args=[self.teenger.username])
#
#         # Make a GET request to the view
#         response = self.client.get(url)
#
#         # Check that the response is successful
#         self.assertEqual(response.status_code, 200)
#         #
#         # # Check that the correct template is used
#         self.assertTemplateUsed(response, 'ourapp/sammaryforteenger.html')
#
#         # Check that teenger_feedback is passed to the template context
#         self.assertIn('teenger_feedback', response.context)
#         #
#         # # Check that the correct teenger is passed to the template context
#         self.assertIn('teenger', response.context)
#         self.assertEqual(response.context['teenger'], self.teenger)
#
#         # Check that teenger_feedback contains the correct feedback
#         teenger_feedback = response.context['teenger_feedback']
#         # self.assertEqual(teenger_feedback1.count(), 2)
#         self.assertIn(self.feedback1, teenger_feedback)
#         self.assertIn(self.feedback2, teenger_feedback)




# class TestSummaryForTeengerView(TestCase):
#     def setUp(self):
#         # Create a test user (teenager)
#         self.teenager = User.objects.create(username='test_teenger')
#         # Create some teenager feedback
#         self.feedback1 = TeengerFeedback.objects.create(Teenger=self.teenager, text="Test Feedback 1", date="2022-03-01", sammary="ff")
#         self.feedback2 = TeengerFeedback.objects.create(Teenger=self.teenager, text="Test Feedback 2", date="2022-04-01", sammary="ff")
#
#     def test_summary_for_teenger_view(self):
#         # URL for the summary for teenager view
#         url = reverse('sammaryforteenger', args=[self.teenager.id])
#
#         # Make a GET request to the view
#         response = self.client.get(url)
#
#         # Check that the response is successful
#         self.assertEqual(response.status_code, 200)
#
#         # Check that the correct template is used
#         self.assertTemplateUsed(response, 'ourapp/sammaryforteenger.html')
#
#         # Check that 'teenger_feedback' and 'Teenger' are in the context
#         self.assertIn('teenger_feedback', response.context)
#         self.assertIn('Teenger', response.context)
#
#         # Check that the correct teenager is passed to the template context
#         self.assertEqual(response.context['Teenger'], self.teenager)
#
#         # Check that teenager feedback contains the correct feedback
#         teenger_feedback = response.context['teenger_feedback']
#         self.assertIn(self.feedback1, teenger_feedback)
#         self.assertIn(self.feedback2, teenger_feedback)


# class AddTeengerFeedbackTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
#
#     def test_add_teenger_feedback_success(self):
#         url = reverse('feedback_teenger')
#         request = self.factory.post(url, {'date': '2024-04-05'})  # Assuming this is today's date
#
#         request.user = self.user
#
#         # Simulate messages
#         setattr(request, 'session', 'session')
#         messages.middleware = FallbackStorage(request)
#         request._messages = messages.storage.fallback.FallbackStorage(request)
#
#         response = add_teenger_feedback(request)
#         self.assertEqual(response.status_code, 200)  # Assuming you are rendering a template upon success
#
#         # Check if feedback was saved
#         self.assertTrue(TeengerFeedback.objects.filter(date='2024-04-05').exists())
#
#     def test_add_teenger_feedback_duplicate_date(self):
#         # Create a TeengerFeedback instance with the same date
#         TeengerFeedback.objects.create(Teenger=self.user, date='2024-04-05', text='Some feedback')
#
#         url = reverse('feedback_teenger')
#         request = self.factory.post(url, {'date': '2024-04-05'})  # Assuming this is today's date
#
#         request.user = self.user
#
#         # Simulate messages
#         setattr(request, 'session', 'session')
#         messages.middleware = FallbackStorage(request)
#         request._messages = messages.storage.fallback.FallbackStorage(request)
#
#         response = add_teenger_feedback(request)
#         self.assertEqual(response.status_code, 302)  # Assuming you are redirecting upon error
#
#         # Check if no new feedback was saved
#         self.assertFalse(TeengerFeedback.objects.filter(date='2024-04-05').exclude(Teenger=self.user).exists())

############################################3
# class AddTeengerFeedbackTestCase(TestCase):
#     def setUp(self):
#         # Setup code if needed
#         pass
#
#     def test_add_teenger_feedback_duplicate_date(self):
#         # Setup
#         TeengerFeedback.objects.create(Teenger='John', text='Test feedback', sammary='Test summary', date='2024-04-05')
#
#         # Get the URL
#         url = reverse('feedback_teenger')
#
#         # Make POST request with duplicate date
#         data = {
#             'date': '2024-04-05',  # Duplicate date
#             # Add other form fields here as needed
#         }
#         response = self.client.post(url, data)
#
#         # Assert redirection to error_teenger
#         self.assertRedirects(response, reverse('error_teenger'))
#
#         # Assert that no new TeengerFeedback object is created
#         self.assertEqual(TeengerFeedback.objects.count(), 1)
#
#     def test_add_teenger_feedback_unique_date(self):
#         # Get the URL
#         url = reverse('feedback_teenger')
#
#         # Make POST request with unique date
#         data = {
#             'date': '2024-04-06',  # Unique date
#             # Add other form fields here as needed
#         }
#         response = self.client.post(url, data)
#
#         # Assert redirection to feedback_teenger
#         self.assertRedirects(response, reverse('feedback_teenger'))
#
#         # Assert that a new TeengerFeedback object is created
#         self.assertEqual(TeengerFeedback.objects.count(), 1)
############################################################3

class Testlist_of_teenger(TestCase):
    def setUp(self):
        self.client = Client()




class Testfeedback_psy_teenger(TestCase):
    def setUp(self):
        self.client = Client()


class Testfeedback_psy_parent(TestCase):
    def setUp(self):
        self.client = Client()

class Testsummary_psy(TestCase):
        def setUp(self):
            self.client = Client()


class Testhome(TestCase):
    def setUp(self):
        self.client = Client()


class Testdrop_down_list_psy(TestCase):
    def setUp(self):
        self.client = Client()


class Testfeedback(TestCase):
    def setUp(self):
        self.client = Client()
class Testlink(TestCase):
    def setUp(self):
        self.client = Client()

class Testtesterforfeed(TestCase):
    def setUp(self):
        self.client = Client()


class Testtest(TestCase):
    def setUp(self):
        self.client = Client()

class Testabes_contact_us(TestCase):
    def setUp(self):
        self.client = Client()

class Testtest_addfeedbackteen(TestCase):
    def setUp(self):
        self.client = Client()


######################################################

# class AddSendSammaryToParentTestCase(TestCase):
#     def setUp(self):
#         # Create a test user
#         self.user = User.objects.create_user(username='test_user', password='test_password')
#         self.client = Client()
#
#         # Create a test parent feedback
#         self.ParentFeedback = ParentFeedback.objects.create(
#             parent='test_user',
#             text='Test feedback',
#             sammary='Test summary',
#             Parents=self.user,
#             date="2022-03-06"
#         )
#
#         # Initialize RequestFactory
#         self.factory = RequestFactory()
#
#     def test_add_send_sammary_to_parent(self):
#         url = reverse('send_sammary_to_parent', kwargs={'username': 'test_user', 'date': self.ParentFeedback.date})
#         request = self.factory.get(url)
#
#         # Simulate POST request
#         form_data = {'sammary': 'Updated summary'}
#         request.user = self.user
#         request.POST = form_data
#         response = add_send_sammary_to_parent(request, username='test_user', date=self.ParentFeedback.date)
#
#         # Check if the form is rendered successfully
#         self.assertEqual(response.status_code, 200)
#
#         # Check if the form is instance of updateparentsammaryForm
#         self.assertIsInstance(response.context['form'], updateparentsammaryForm)
#
#         # Check if the form is saved successfully
#         self.assertTrue(ParentFeedback.objects.filter(sammary='Updated summary').exists())
#
#         # Check if the success message is displayed
#         messages = list(response.context['messages'])
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(messages[0].tags, 'success')
#         self.assertEqual(messages[0].message, 'summary sent successfully!')
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
    # def test_add_send_sammary_to_parent_invalid_form(self):
    #     url = reverse('send_sammary_to_parent', kwargs={'username': 'test_user', 'date': self.parent_feedback.date})
    #     request = self.factory.post(url)
    #
    #     # Simulate invalid form data
    #     form_data = {}  # Empty form data
    #     request.user = self.user
    #     request.POST = form_data
    #     response = add_send_sammary_to_parent(request, username='test_user', date=self.parent_feedback.date)
    #
    #     # Check if the form is rendered again with errors
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsInstance(response.context['form'], updateparentsammaryForm)
    #     self.assertTrue(response.context['form'].errors)
    #
    #     # Check if the parent feedback is not updated
    #     self.assertEqual(ParentFeedback.objects.get(pk=self.parent_feedback.pk).sammary, 'Test summary')
    #
    # def test_add_send_sammary_to_parent_invalid_user(self):
    #     url = reverse('send_sammary_to_parent', kwargs={'username': 'invalid_user', 'date': self.parent_feedback.date})
    #     request = self.factory.post(url)
    #
    #     # Simulate POST request with invalid user
    #     form_data = {'sammary': 'Updated summary'}
    #     request.user = self.user  # Set a different user
    #     request.POST = form_data
    #     response = add_send_sammary_to_parent(request, username='invalid_user', date=self.parent_feedback.date)
    #
    #     # Check if the response is a redirect
    #     self.assertRedirects(response, reverse('error_page'))  # Assuming there is an 'error_page' URL configured
    #
    #     # Check if the parent feedback is not updated
    #     self.assertEqual(ParentFeedback.objects.get(pk=self.parent_feedback.pk).sammary, 'Test summary')