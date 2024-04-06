from django.template.response import TemplateResponse
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
from ourapp.views import error_parent, error_teenager, contact_teens


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view_post(self):
        data = {'username': 'newusername', 'email': 'newemail@example.com'}
        response = self.client.post(reverse('profile'), data)
        self.assertEqual(response.status_code, 302)

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newusername')
        self.assertEqual(self.user.email, 'newemail@example.com')

    def test_profile_view_get(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

        self.assertTrue('u_form' in response.context)
        self.assertTrue('p_form' in response.context)
        self.assertIsInstance(response.context['u_form'], UpdateUserForm)
        self.assertIsInstance(response.context['p_form'], profileupdateform)

class NavbarForPsyTestCase(TestCase):
    def test_navbarforpsy_view(self):
        response = self.client.get(reverse('navbarforpsy'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'ourapp/navbarforpsy.html')

class HomepageForPsyTestCase(TestCase):
    def test_homepageforpsy_view(self):
        response = self.client.get(reverse('homepageforpsy'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'ourapp/homepageforpsy.html')


class TestLoginParent(TestCase):
    def setUp(self):
        self.client = Client()
        self.group = Group.objects.create(name='Parents')
        self.user = User.objects.create_user(username='test_parent', password='testpassword')
        self.group.user_set.add(self.user)

    def test_login_successful(self):
        response = self.client.post(reverse('loginParent'), {'username': 'test_parent', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Should redirect to homepage_parent

    def test_login_unsuccessful(self):
        response = self.client.post(reverse('loginParent'), {'username': 'incorrect_username', 'password': 'incorrect_password'})
        self.assertEqual(response.status_code, 200)  # Should stay on the login page
        self.assertContains(response, 'username OR password incorrert')

    def test_login_non_parent_user(self):
        non_parent_user = User.objects.create_user(username='non_parent_user', password='testpassword')
        response = self.client.post(reverse('loginParent'), {'username': 'non_parent_user', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)  # Should stay on the login page
        self.assertContains(response, 'username OR password incorrert')

class TestHomepageTeenager(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_teenager_view(self):
        response = self.client.get(reverse('homepage_teenager'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/homepage_teenager.html')

class TestNavbarTeenager(TestCase):
    def setUp(self):
        self.client = Client()

    def test_navbar_teenager_view(self):
        response = self.client.get(reverse('navbar_teenager'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/navbar_teenager.html')

class TestHomepageParent(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_parent_view(self):
        response = self.client.get(reverse('homepage_parent'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/homepage_parent.html')


class LogoutParentTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    def test_logout_parent_view(self):
        response = self.client.get(reverse('logout_parent'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/logout_parent.html')




class LogoutTeenagesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    def test_logout_teenagers_view(self):
        response = self.client.get(reverse('logout_teens'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/logout_teens.html')



class LogoutPsychologistTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    def test_logout_psychologist_view(self):
        response = self.client.get(reverse('logout_psy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/logout_psy.html')


class ErrorParentViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_error_parent_view(self):
        request = self.factory.get('error_parent')
        response = error_parent(request)
        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.template_name, 'ourapp/error_parent.html')


class TestErrorTeenagerView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_error_teenager_view(self):
        request = self.factory.get('error_teenager')
        response = error_teenager(request)
        self.assertEqual(response.status_code, 200)


class AboutPageTest(TestCase):
    def test_about_page_returns_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ourapp/About.html')


class TestContactTeensView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_contact_teens_view(self):
        request = self.factory.get('/contact_teens/')
        response = contact_teens(request)
        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'ourapp/contact_teens.html')