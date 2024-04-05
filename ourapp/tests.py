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
from django.test import Client
from django.shortcuts import get_object_or_404
from .models import Lecture
from django.conf import settings
from .views import choicelinktopic_teenager, choicelinktopic_parent



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







