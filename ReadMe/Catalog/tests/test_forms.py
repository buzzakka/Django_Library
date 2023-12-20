import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from Catalog.forms import *
from Catalog.models import *

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)

@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class AddGenreFormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = AddGenreForm()
    
    def setUp(self):
        self.user = get_user_model().objects.create(username="client_user")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

        perm = Permission.objects.get(codename='add_genre')
        self.user.user_permissions.add(perm)

    def test_add_genre(self):
        genres_count = Genre.objects.count()
        
        form_data = {'genre': 'test_genre'}
        
        self.authorized_client.post(
            reverse('add_genre'),
            data=form_data
        )
        
        self.assertEqual(Genre.objects.count(), genres_count + 1)
        self.assertTrue(Genre.objects.filter(genre='test_genre').exists())
    
    def test_add_genre_unique_genre_error(self):
        genres_count = Genre.objects.count()
        
        form_data = {'genre': 'test_genre'}
        
        self.authorized_client.post(
            reverse('add_genre'),
            data=form_data
        )
        response = self.authorized_client.post(
            reverse('add_genre'),
            data=form_data
        )
        self.assertFormError(
            response,
            'form',
            'genre',
            'Такой жанр уже существует'
        )
        
        self.assertEqual(Genre.objects.count(), genres_count + 1)
        # self.assertTrue(Genre.objects.filter(genre='test_genre').exists())
        
    # def test_title_field_label(self):
    #     self.assertEqual(self.form.fields['title'].label, "Название")
    
    # def test_author_field_label(self):
    #     self.assertEqual(self.form.fields['author'].label, "Автор")
    
    # def test_genre_field_label(self):
    #     self.assertEqual(self.form.fields['genre'].label, "Жанр")
    
    # def test_about_field_label(self):
    #     self.assertEqual(self.form.fields['about'].label, "Описание книги")
    
    # def test_link_to_file_field_label(self):
    #     self.assertEqual(self.form.fields['link_to_file'].label, "Путь до файла")
    
    # def test_image_field_label(self):
    #     self.assertEqual(self.form.fields['image'].label, "Изображение")