from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

from Catalog.models import *
from .test_constants import *

from slugify import slugify
from os import path
from shutil import rmtree


class GenreModelTest(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(genre=GENRE_NAME)

    def test_genre_verbose(self):
        self.assertEqual(self.genre._meta.get_field("genre").verbose_name, "Жанр")
    
    def test_genre_max_length(self):
        self.assertEqual(self.genre._meta.get_field("genre").max_length, 200)
    
    def test_slug_max_length(self):
        self.assertEqual(self.genre._meta.get_field("slug").max_length, 200)
    
    def test_is_correct_slug(self):
        self.assertEqual(self.genre.slug, slugify(GENRE_NAME))
    
    def test_is_correct_str(self):
        self.assertTrue(str(self.genre), GENRE_NAME)

class AuthorModelTest(TestCase):
    
    def setUp(self):
        self.author = Author.objects.create(
            first_name=AUTHOR_FIRST_NAME,
            last_name=AUTHOR_LAST_NAME,
            date_of_birth=AUTHOR_DATE_OF_BIRTH,
            about=AUTHOR_ABOUT,
            image=SimpleUploadedFile("test.png", b"info")
        )
        rmtree(path.dirname(self.author.image.path))
    
    def test_first_name_verbose(self):
        self.assertEqual(self.author._meta.get_field("first_name").verbose_name, "Имя")
    
    def test_first_name_max_length(self):
        self.assertEqual(self.author._meta.get_field("first_name").max_length, 200)

    def test_last_name_verbose(self):
        self.assertEqual(self.author._meta.get_field("last_name").verbose_name, "Фамилия")
    
    def test_last_name_max_length(self):
        self.assertEqual(self.author._meta.get_field("last_name").max_length, 200)

    def test_date_of_birth_meta(self):
        self.assertEqual(self.author._meta.get_field("date_of_birth").verbose_name, "Дата рождения")
    
    def test_date_of_death_verbose(self):
        self.assertEqual(self.author._meta.get_field("date_of_death").verbose_name, "Дата смерти")
        
    def test_about_max_length(self):
        self.assertEqual(self.author._meta.get_field("about").max_length, 1000)
    
    def test_about_default(self):
        self.assertEqual(self.author._meta.get_field("about").default, "")
    
    def test_about_verbose(self):
        self.assertEqual(self.author._meta.get_field("about").verbose_name, "Об авторе")
    
    def test_image_verbose(self):
        self.assertEqual(self.author._meta.get_field("image").verbose_name, "Изображение")
    
    def test_is_correct_first_name(self):
        self.assertEqual(self.author.first_name, AUTHOR_FIRST_NAME)
        
    def test_is_correct_last_name(self):
        self.assertEqual(self.author.last_name, AUTHOR_LAST_NAME)
    
    def test_is_correct_slug(self):
        correct_slug = slugify(f"{self.author.first_name} {self.author.last_name}")
        self.assertEqual(self.author.slug, correct_slug)
    
    def test_is_correct_date_of_birth(self):
        self.assertEqual(self.author.date_of_birth, AUTHOR_DATE_OF_BIRTH)
        
    def test_is_correct_date_of_death(self):
        self.assertIsNone(self.author.date_of_death)
    
    def test_is_correct_about(self):
        self.assertEqual(self.author.about, AUTHOR_ABOUT)
    
    def test_is_correct_image_path(self):
        new_filename = f"{self.author.slug}.png"
        correct_path = f"{path.abspath('.')}/media/authors/{self.author.slug}/{new_filename}"
        self.assertEqual(self.author.image.path, correct_path)
    
    def test_get_absolute_url(self):
        correct_url = f"/author/{self.author.slug}"
        self.assertEqual(self.author.get_absolute_url(), correct_url)
    
    def test_is_correct_str(self):
        self.assertEqual(str(self.author), f"{AUTHOR_LAST_NAME} {AUTHOR_FIRST_NAME}")

class BookModelTest(TestCase):
    
    def setUp(self):
        Genre.objects.create(genre='test_genre_1')
        Genre.objects.create(genre='test_genre_2')
        self.author = Author.objects.create(
            first_name="first_name",
            last_name="last_name",
            date_of_birth="2023-10-10"
        )
        self.book = Book.objects.create(
            title=BOOK_TITLE,
            author=self.author,
            about=BOOK_ABOUT,
            link_to_file=SimpleUploadedFile("test.pdf", b"file info"),
            image=SimpleUploadedFile("test.png", b"png info")
        )
        rmtree(path.dirname(self.book.link_to_file.path))
        self.book.genre.set(Genre.objects.all())
        self.book.save()
    
    def test_title_verbose(self):
        self.assertEqual(self.book._meta.get_field("title").verbose_name, "Название")
    
    def test_title_max_length(self):
        self.assertEqual(self.book._meta.get_field("title").max_length, 200)

    def test_author_verbose(self):
        
        self.assertEqual(self.book._meta.get_field("author").verbose_name, "Автор")
    
    def test_genre_verbose(self):
        
        self.assertEqual(self.book._meta.get_field("genre").verbose_name, 'Жанр')
    
    def test_about_verbose(self):
        
        self.assertEqual(self.book._meta.get_field("about").verbose_name, 'Описание книги')
    
    def test_about_max_length(self):
        
        self.assertEqual(self.book._meta.get_field("about").max_length, 1000)
    
    def test_rating_verbose(self):
        
        self.assertEqual(self.book._meta.get_field("rating").verbose_name, 'Рейтинг')
    
    def test_rating_default(self):
        
        self.assertEqual(self.book.rating, 0)
    
    def test_link_to_file_verbose(self):
        
        self.assertEqual(self.book._meta.get_field("link_to_file").verbose_name, 'Путь до файла')
    
    def test_image_verbose(self):
        
        self.assertEqual(self.book._meta.get_field("image").verbose_name, 'Изображение')
    
    def test_is_correct_title(self):
        self.assertEqual(self.book.title, BOOK_TITLE)
    
    def test_is_correct_slug(self):
        self.assertEqual(self.book.slug, slugify(self.book.title))
    
    def test_is_correct_author(self):
        self.assertEqual(self.book.author, self.author)
    
    def test_is_correct_genre(self):
        genres = Genre.objects.all()
        self.assertCountEqual(list(self.book.genre.all()), list(genres))
    
    def test_is_correct_about(self):
        self.assertEqual(self.book.about, BOOK_ABOUT)
    
    def test_is_correct_rating(self):
        self.assertEqual(self.book.rating, 0)
   
    def test_is_correct_image(self):
        new_filename = f"{self.book.slug}.png"
        correct_path = f"{path.abspath('.')}/media/books/{self.book.slug}/{new_filename}"
        self.assertEqual(self.book.image.path, correct_path)
    
    def test_is_correct_link_to_file(self):
        new_filename = f"{self.book.slug}.pdf"
        correct_path = f"{path.abspath('.')}/media/books/{self.book.slug}/{new_filename}"
        self.assertEqual(self.book.link_to_file.path, correct_path)
    
    def test_get_absolute_url(self):
        correct_url = f"/book/{self.book.slug}"
        self.assertEqual(self.book.get_absolute_url(), correct_url)
    
    def test_is_correct_str(self):
        self.assertEqual(str(self.book), BOOK_TITLE)

class BookshelfTest(TestCase):

    def setUp(self):
        Genre.objects.create(genre='test_genre_1')
        self.author = Author.objects.create(
            first_name=f"{AUTHOR_FIRST_NAME}",
            last_name=f"{AUTHOR_LAST_NAME}",
            date_of_birth=f"{AUTHOR_DATE_OF_BIRTH}"
        )
        self.book = Book.objects.create(title=BOOK_TITLE, author=self.author,)
        
        self.user, created = get_user_model().objects.get_or_create(username=USER_USERNAME, email=USER_EMAIL, password=USER_PASSWORD)
        self.bookshelf, created = Bookshelf.objects.get_or_create(user=self.user)
        self.bookshelf.book.add(self.book)
        
    def test_user_verbose(self):
        self.assertEqual(self.bookshelf._meta.get_field("user").verbose_name, "Пользователь")
    
    def test_book_verbose(self):
        self.assertEqual(self.bookshelf._meta.get_field("book").verbose_name, "Книга")
    
    def test_is_correct_user(self):
        self.assertEqual(self.bookshelf.user, self.user)
        self.assertEqual(self.bookshelf.user.get_username(), USER_USERNAME)
    
    def test_is_correct_book(self):
        books = Book.objects.all()
        self.assertCountEqual(list(self.bookshelf.book.all()), list(books))
    
    def test_is_correct_str(self):
        self.assertEqual(str(self.bookshelf), f'Книжная полка пользователя {self.user}')