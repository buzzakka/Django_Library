from django.test import TestCase
from Catalog.models import *
from slugify import slugify
from .test_constants import *
from datetime import datetime
from os import path


class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(genre=GENRE_NAME)

    def test_genre_verbose(self):
        genre = Genre.objects.get(id=1)
        self.assertEqual(genre._meta.get_field("genre").verbose_name, "Жанр")
    
    def test_is_correct_slug(self):
        genre = Genre.objects.get(id=1)
        self.assertEqual(genre.slug, slugify(GENRE_NAME))
    
    def test_is_correct_str(self):
        genre = Genre.objects.get(id=1)
        self.assertTrue(str(genre), GENRE_NAME)


class AuthorModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            first_name=AUTHOR_FIRST_NAME,
            last_name=AUTHOR_LAST_NAME,
            date_of_birth=AUTHOR_DATE_OF_BIRTH,
            about=AUTHOR_ABOUT,
            image=IMG_PATH
        )
    
    def test_first_name_verbose(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author._meta.get_field("first_name").verbose_name, "Имя")

    def test_last_name_verbose(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author._meta.get_field("last_name").verbose_name, "Фамилия")

    def test_date_of_birth_meta(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author._meta.get_field("date_of_birth").verbose_name, "Дата рождения")
    
    def test_date_of_death_verbose(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author._meta.get_field("date_of_death").verbose_name, "Дата смерти")
    
    def test_about_meta(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author._meta.get_field("about").default, "")
        self.assertEqual(author._meta.get_field("about").verbose_name, "Об авторе")
    
    def test_image_verbose(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author._meta.get_field("image").verbose_name, "Изображение")
    
    def test_is_correct_first_name(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.first_name, AUTHOR_FIRST_NAME)
        
    def test_is_correct_last_name(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.last_name, AUTHOR_LAST_NAME)
    
    def test_is_correct_slug(self):
        author = Author.objects.get(id=1)
        correct_slug = slugify(f"{author.first_name} {author.last_name}")
        self.assertEqual(author.slug, correct_slug)
    
    def test_is_correct_date_of_birth(self):
        author = Author.objects.get(id=1)
        correct_date = datetime.strptime(AUTHOR_DATE_OF_BIRTH, '%Y-%m-%d').date()
        self.assertEqual(author.date_of_birth, correct_date)
        
    def test_is_correct_date_of_death(self):
        author = Author.objects.get(id=1)
        self.assertIsNone(author.date_of_death)
    
    def test_is_correct_about(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.about, AUTHOR_ABOUT)
    
    def test_is_correct_image_path(self):
        author = Author.objects.get(id=1)
        correct_path = f"{path.abspath('.')}/media/{IMG_PATH}"
        self.assertEqual(author.image.path, correct_path)
    
    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        correct_url = f"/author/{author.slug}"
        self.assertEqual(author.get_absolute_url(), correct_url)
    
    def test_is_correct_str(self):
        author = Author.objects.get(id=1)
        self.assertEqual(str(author), f"{author.last_name} {author.first_name}")
    
    