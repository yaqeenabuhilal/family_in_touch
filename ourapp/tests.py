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

class TestLoginPsychologist(TestCase):
    def setUp(self):
        self.url = reverse('login psychologist')
        self.user = User.objects.create_user(username='test_user', password='test_password')
        Group.objects.create(name='Psychotherapist').user_set.add(self.user)

    def test_login_successful(self):
        # בדיקה כאשר הפרטים שהוזנו הם נכונים
        response = self.client.post(self.url, {'username': 'test_user', 'password': 'test_password'})
        self.assertRedirects(response, reverse('dashboard'))

    def test_login_unsuccessful(self):
        # בדיקה כאשר שם המשתמש או הסיסמה אינם נכונים
        response = self.client.post(self.url, {'username': 'incorrect_username', 'password': 'incorrect_password'})
        self.assertContains(response, 'username OR password incorrect')
