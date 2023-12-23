import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model

from users.models import User


class TestRegisterUserForm(TestCase):

    def setUp(self):
        super().setUp()
        self.guest_client = Client()

    def test_register_form(self):
        self.assertFalse(
            get_user_model().objects.filter(
                username='user',
                email='user@mail.ru'
            ).exists()
        )

        form_data = {
            'username': 'user',
            'email': 'user@mail.ru',
            'password1': 'useruser',
            'password2': 'useruser'
        }

        self.guest_client.post(
            reverse('users:register'),
            data=form_data
        )
        self.assertTrue(
            get_user_model().objects.filter(
                username='user',
                email='user@mail.ru'
            ).exists()
        )

    def test_register_form_unique_email_error(self):
        form_data = {
            'username': 'user',
            'email': 'user@mail.ru',
            'password1': 'useruser',
            'password2': 'useruser'
        }

        self.guest_client.post(
            reverse('users:register'),
            data=form_data
        )
        self.assertTrue(
            get_user_model().objects.filter(
                username='user',
                email='user@mail.ru'
            ).exists()
        )
        response = self.guest_client.post(
            reverse('users:register'),
            data=form_data
        )
        self.assertFormError(
            response,
            'form',
            'email',
            'Пользователь с таким E-mail уже существует'
        )


TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class TestEditProfileForm(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = get_user_model().objects.create(username="client_user")
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)

        cls.small_png = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )

        cls.uploaded_image = SimpleUploadedFile(
            name='photo.png',
            content=cls.small_png,
            content_type='image/gif'
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def test_edit_profile_form(self):
        user = User.objects.get(username="client_user")
        form_data = {
            'first_name': 'Igor',
            'last_name': 'test',
            'image': self.uploaded_image
        }

        response = self.authorized_client.post(
            reverse('users:edit-profile'),
            data=form_data,
            # format='multipart'
        )

        user.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:profile'))
        self.assertEqual(user.first_name, 'Igor')
        self.assertEqual(user.last_name, 'test')
        self.assertEqual(user.image.url, '/media/user/client_user/photo.png')
