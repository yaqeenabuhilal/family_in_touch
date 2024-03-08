from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

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


