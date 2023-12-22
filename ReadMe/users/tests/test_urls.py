from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from Catalog.views import *

class TestUsersUrl(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = get_user_model().objects.create(username="client_user")
    
    def setUp(self):
        self.unauthorized_client = Client()

        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    '''
        url = 'login/'
    '''
    def test_login_page_with_unauthorized_user(self):
        response = self.unauthorized_client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
    
    def test_login_page_with_authorized_user(self):
        response = self.authorized_client.get(reverse('users:login'))
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(response.status_code, 302)
    
    '''
        url = 'logout/'
    '''
    def test_logout_page_with_unauthorized_user(self):
        response = self.unauthorized_client.get(reverse('users:logout'))
        self.assertRedirects(response, reverse('users:login'))
        self.assertEqual(response.status_code, 302)
    
    def test_logout_page_with_authorized_user(self):
        response = self.authorized_client.get(reverse('users:logout'))
        self.assertRedirects(response, reverse('users:login'))
        self.assertEqual(response.status_code, 302)
    
    '''
        url = 'register/'
    '''
    def test_register_page_with_unauthorized_user(self):
        response = self.unauthorized_client.get(reverse('users:register'))
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertEqual(response.status_code, 200)
    
    def test_register_page_with_authorized_user(self):
        response = self.authorized_client.get(reverse('users:register'))
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(response.status_code, 302)
    
    '''
        url = 'profile/'
    '''
    def test_profile_page_with_unauthorized_user(self):
        response = self.unauthorized_client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('users:login')}?next=/users/profile/")
    
    def test_profile_page_with_authorized_user(self):
        response = self.authorized_client.get(reverse('users:profile'))
        self.assertTemplateUsed(response, 'users/profile.html')
        self.assertEqual(response.status_code, 200)
    
    '''
        url = 'profile/edit/'
    '''
    def test_edit_profile_page_with_unauthorized_user(self):
        response = self.unauthorized_client.get(reverse('users:edit-profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('users:login')}?next=/users/profile/edit/")
    
    def test_edit_profile_page_with_authorized_user(self):
        response = self.authorized_client.get(reverse('users:edit-profile'))
        self.assertTemplateUsed(response, 'users/edit_profile.html')
        self.assertEqual(response.status_code, 200)
    
    '''
        url = 'profile/change-password/'
    '''
    def test_change_password_page_with_unauthorized_user(self):
        response = self.unauthorized_client.get(reverse('users:change-password'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('users:login')}?next=/users/profile/change-password/")
    
    def test_change_password_page_with_authorized_user(self):
        response = self.authorized_client.get(reverse('users:change-password'))
        self.assertTemplateUsed(response, 'users/change_password.html')
        self.assertEqual(response.status_code, 200)
    
    '''
        url = 'profile/delete/'
    '''
    def test_delete_page_with_unauthorized_user(self):
        response = self.unauthorized_client.get(reverse('users:delete'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('users:login')}?next=/users/profile/delete/")
    
    def test_delete_page_with_authorized_user(self):
        response = self.authorized_client.get(reverse('users:delete'))
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(response.status_code, 302)