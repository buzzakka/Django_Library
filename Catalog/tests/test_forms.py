import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.contrib.auth.models import Permission

from Catalog.models import *

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class AddGenreFormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create(username="client_user")
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)

        perm = Permission.objects.get(codename='add_genre')
        cls.user.user_permissions.add(perm)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def test_add_genre_form(self):
        genres_count = Genre.objects.count()

        form_data = {'genre': 'test_genre'}

        self.authorized_client.post(
            reverse('catalog:add_genre'),
            data=form_data
        )

        self.assertEqual(Genre.objects.count(), genres_count + 1)
        self.assertTrue(Genre.objects.filter(genre='test_genre').exists())

    def test_add_genre_form_unique_genre_error(self):
        genres_count = Genre.objects.count()

        form_data = {'genre': 'test_genre'}

        self.authorized_client.post(
            reverse('catalog:add_genre'),
            data=form_data
        )
        response = self.authorized_client.post(
            reverse('catalog:add_genre'),
            data=form_data
        )
        self.assertFormError(
            response,
            'form',
            'genre',
            'Такой жанр уже существует'
        )

        self.assertEqual(Genre.objects.count(), genres_count + 1)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class AddAuthorFormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create(username="client_user")
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)

        perm = Permission.objects.get(codename='add_author')
        cls.user.user_permissions.add(perm)

        cls.small_png = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )

        cls.uploaded_image = SimpleUploadedFile(
            name='small.gif',
            content=cls.small_png,
            content_type='image/gif'
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def test_add_author_form(self):
        authors_count = Author.objects.count()

        form_data = {
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'date_of_birth': '1864-10-10',
            'date_of_death': '2023-10-10',
            'about': 'test_text_about_author',
            'image': self.uploaded_image,
        }
        response = self.authorized_client.post(
            reverse('catalog:add_author'),
            data=form_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Author.objects.count(), authors_count + 1)

    # def test_add_author_unique_author_error(self):
    #     form_data = {
    #         'first_name': 'test_first_name',
    #         'last_name': 'test_last_name',
    #         'date_of_birth': '1865-10-10',
    #         'date_of_death': '2000-10-10',
    #         'about': 'test_text_about_author',
    #         'image': self.uploaded_image,
    #     }
    #     self.authorized_client.post(
    #         reverse('add_author'),
    #         data=form_data
    #     )
    #     authors_count = Author.objects.count()
    #     response = self.authorized_client.post(
    #         reverse('add_author'),
    #         data=form_data
    #     )
    #     self.assertFormError(
    #         response,
    #         'form',
    #         None,
    #         'Такой автор уже существует'
    #     )
    #     self.assertEqual(Author.objects.count(), authors_count)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class AddBookFormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create(username="client_user")
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)

        perm = Permission.objects.get(codename='add_book')
        cls.user.user_permissions.add(perm)

        cls.small_png = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )

        cls.uploaded_image = SimpleUploadedFile(
            name='small.gif',
            content=cls.small_png,
            content_type='image/gif'
        )
        cls.uploaded_file = SimpleUploadedFile(
            name="book.pdf",
            content=cls.small_png,
            content_type='image/gif'
        )

        cls.author = Author.objects.create(
            first_name="test",
            last_name="test",
            date_of_birth="2023-10-10"
        )
        cls.genre = Genre.objects.create(genre="test_genre")

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def test_add_book_form(self):
        books_count = Book.objects.count()

        form_data = {
            'title': 'test',
            'author': self.author.pk,
            'genre': [self.genre.pk],
            'about': 'long_text',
            'link_to_file': self.uploaded_file,
            'image': self.uploaded_image,
        }
        self.authorized_client.post(
            reverse('catalog:add_book'),
            data=form_data
        )
        self.assertEqual(Book.objects.count(), books_count + 1)

        books_count = Book.objects.count()

        self.assertTrue(Book.objects.filter(title='test').exists())

        response = self.authorized_client.post(
            reverse('catalog:add_book'),
            data=form_data
        )
        self.assertFormError(
            response,
            'form',
            'title',
            'Такая книга уже существует'
        )
        self.assertEqual(Book.objects.count(), books_count)
