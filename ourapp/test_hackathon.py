from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
class TestLoginPsychologist(TestCase):
    def setUp(self):
        self.url = reverse('loginpsychologist')
        self.user = User.objects.create_user(username='test_user', password='test_password')
        Group.objects.create(name='Psychotherapist').user_set.add(self.user)

    def test_login_successful(self):
        # בדיקה כאשר הפרטים שהוזנו הם נכונים
        response = self.client.post(self.url, {'username': 'test_user', 'password': 'test_password'})
        self.assertRedirects(response, reverse('dashbord'))

    def test_login_unsuccessful(self):
        # בדיקה כאשר שם המשתמש או הסיסמה אינם נכונים
        response = self.client.post(self.url, {'username': 'incorrect_username', 'password': 'incorrect_password'})
        self.assertContains(response, 'username OR password incorrect')
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import unittest
import re
from django.test import RequestFactory
from ourapp.views import loginParent

class TestLoginParents(TestCase):
    def setUp(self):
        self.url = reverse('loginParent')
        self.user = User.objects.create_user(username='test_user', password='test_password')
        Group.objects.create(name='Parents').user_set.add(self.user)
    def test_login_successful(self):
        # בדיקה כאשר הפרטים שהוזנו הם נכונים
        response = self.client.post(self.url, {'username': 'test_user', 'password': 'test_password'})
        self.assertRedirects(response, reverse('dashbord'))
    def test_login_unsuccessful(self):
        # בדיקה כאשר שם המשתמש או הסיסמה אינם נכונים
        response = self.client.post(self.url, {'username': 'incorrect_username', 'password': 'incorrect_password'})
        self.assertContains(response, 'username OR password incorrert')

class TestSignUpParents(TestCase):
    def setUp(self):
        self.url = reverse('sign_up_parent')
        self.user = User.objects.create_user(username='test_user', password='test_password')

        # בדיקה אם הקבוצה כבר קיימת ורק אז יוצרים אותה
        if not Group.objects.filter(name='Parents').exists():
            group = Group.objects.create(name='Parents')
            group.user_set.add(self.user)
        else:
            group = Group.objects.get(name='Parents')
            group.user_set.add(self.user)
    def test_signup_invalid_form(self):
        # בדיקה כאשר ניסיון ליצור משתמש הורה עם פרטים לא תקינים
        response = self.client.post(self.url,{'username': '', 'password1': 'test_password123', 'password2': 'test_password123'})
        self.assertContains(response, 'This field is required.')

class TestLoginTeenager(TestCase):
    def setUp(self):
        self.url = reverse('loginTeenager')
        self.user = User.objects.create_user(username='test_user', password='test_password')
        Group.objects.create(name='Teengers').user_set.add(self.user)

    def test_login_successful(self):
        # בדיקה כאשר הפרטים שהוזנו הם נכונים
        response = self.client.post(self.url, {'username': 'test_user', 'password': 'test_password'})
        self.assertRedirects(response, reverse('dashbord'))

    def test_login_unsuccessful(self):
        # בדיקה כאשר שם המשתמש או הסיסמה אינם נכונים
        response = self.client.post(self.url, {'username': 'incorrect_username', 'password': 'incorrect_password'})
        self.assertContains(response, 'username OR password incorrert')

###############################################################


class TestLoginTeenagerai(TestCase):
    def setUp(self):
        self.url = reverse('loginTeenager')
        self.user = User.objects.create_user(username='testuser', password='password123')
        Group.objects.create(name='Teengers').user_set.add(self.user)
    def test_login_success(self):
        response = self.client.post('/loginTeenager/', {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)
        # self.assertContains(response, 'Login successful')
    #
    def test_login_failure(self):
        response = self.client.post('/loginTeenager/', {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Login failed')

    def test_empty_fields(self):
        response = self.client.post('/loginTeenager/', {'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Please fill in all fields')

class TestLoginPsychologist(TestCase):
    def setUp(self):
        self.url = reverse('loginpsychologist')
        self.user = User.objects.create_user(username='test_user', password='test_password')
        Group.objects.create(name='Psychotherapist').user_set.add(self.user)

    def test_login_successful(self):
        # בדיקה כאשר הפרטים שהוזנו הם נכונים
        response = self.client.post(self.url, {'username': 'test_user', 'password': 'test_password'})
        self.assertRedirects(response, reverse('dashbord'))

    def test_login_unsuccessful(self):
        # בדיקה כאשר שם המשתמש או הסיסמה אינם נכונים
        response = self.client.post(self.url, {'username': 'incorrect_username', 'password': 'incorrect_password'})
        self.assertContains(response, 'username OR password incorrert')




#בדיקות יחידה AI
def is_username_empty(username):
    return bool(username)  # בודק האם המחרוזת של שם המשתמש אינה ריקה


class TestUsername(unittest.TestCase):
    def test_non_empty_username(self):
        self.assertTrue(is_username_empty("user123"))  # בודק אם שם המשתמש אינו ריק

    def test_empty_username(self):
        self.assertFalse(is_username_empty(""))  # בודק אם שם המשתמש ריק


def is_password_empty(password):
    return bool(password)  # בודק האם המחרוזת של הסיסמה אינה ריקה
class TestPassword(unittest.TestCase):
    def test_non_empty_password(self):
        self.assertTrue(is_password_empty("SecurePassword123"))  # בודק אם הסיסמה אינה ריקה

    def test_empty_password(self):
        self.assertFalse(is_password_empty(""))  # בודק אם הסיסמה ריקה


def is_whitespace_included(password):
    return ' ' not in password  # בודק האם יש רווחים בסיסמה

class TestPassword(unittest.TestCase):
    def test_password_with_no_whitespace(self):
        self.assertTrue(is_whitespace_included("Password123"))  # בודק אם הסיסמה אינה מכילה רווחים
    def test_password_with_whitespace(self):
        self.assertFalse(is_whitespace_included("Pass word123"))  # בודק אם הסיסמה מכילה רווחים