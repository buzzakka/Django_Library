from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from Catalog.views import *
from .constants import *

class TestUrl(TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        Genre.objects.create(
            genre=GENRE_NAME
        )
        author = Author.objects.create(
            first_name=AUTHOR_FIRST_NAME,
            last_name=AUTHOR_LAST_NAME,
            date_of_birth=AUTHOR_DATE_OF_BIRTH
        )
        book = Book.objects.create(
            title=BOOK_TITLE,
            author=author
        )
        book.genre.set(Genre.objects.all())
    
    def setUp(self):
        self.guest_client = Client()

        self.user = get_user_model().objects.create(username="client_user")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
    
    '''
        url = '/'
    '''
    def test_index_url_exists_at_desired_location(self):
        response = self.guest_client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_index_url_uses_correct_template(self):
        response = self.guest_client.get(reverse('index'))
        self.assertTemplateUsed(response, 'catalog/index.html')
    
    '''
        url = '/authors/'
    '''
    def test_authors_url_exists_at_desired_location(self):
        response = self.guest_client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
    
    def test_authors_url_uses_correct_template(self):
        response = self.guest_client.get(reverse('authors'))
        self.assertTemplateUsed(response, 'catalog/authors/author_list.html')
    
    '''
        url = '/authors/add_author'
    '''
    def test_add_author_url_exists_at_desired_location_anonymous_user(self):
        response = self.guest_client.get(reverse('add_author'))
        self.assertEqual(response.status_code, 302)
    
    def test_add_author_url_exists_at_desired_location_authorized_user_without_perms(self):
        response = self.authorized_client.get(reverse('add_author'))
        self.assertEqual(response.status_code, 403)
    
    def test_add_author_url_exists_at_desired_location_authorized_user_with_perms(self):
        perm = Permission.objects.get(codename='add_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('add_author'))
        self.assertEqual(response.status_code, 200)

    def test_add_author_url_uses_correct_template(self):
        perm = Permission.objects.get(codename='add_author')    
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('add_author'))
        self.assertTemplateUsed(response, 'catalog/authors/add_author.html')

    '''
        url = 'author/<slug:slug>'
    '''
    def test_author_url_exists_at_desired_location(self):
        slug = Author.objects.get(first_name=AUTHOR_FIRST_NAME).slug
        response = self.guest_client.get(reverse('author_detail', args=[slug]))
        self.assertEqual(response.status_code, 200)
    
    def test_author_url_uses_correct_template(self):
        slug = Author.objects.get(first_name=AUTHOR_FIRST_NAME).slug
        response = self.guest_client.get(reverse('author_detail', args=[slug]))
        self.assertTemplateUsed(response, 'catalog/authors/author_detail.html')

    '''
        url = 'author/<slug:slug>/edit'
    '''
    def test_edit_author_url_exists_at_desired_location_anonymous_user(self):
        slug = Author.objects.get(first_name=AUTHOR_FIRST_NAME).slug
        response = self.guest_client.get(reverse('edit_author', args=[slug]))
        self.assertEqual(response.status_code, 302)
    
    def test_edit_author_url_exists_at_desired_location_authorized_user_without_perms(self):
        slug = Author.objects.get(first_name=AUTHOR_FIRST_NAME).slug
        response = self.authorized_client.get(reverse('edit_author', args=[slug]))
        self.assertEqual(response.status_code, 403)
    
    def test_edit_author_url_exists_at_desired_location_authorized_user_with_perms(self):
        slug = Author.objects.get(first_name=AUTHOR_FIRST_NAME).slug
        perm = Permission.objects.get(codename='change_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('edit_author', args=[slug]))
        self.assertEqual(response.status_code, 200)

    def test_edit_author_url_uses_correct_template(self):
        slug = Author.objects.get(first_name=AUTHOR_FIRST_NAME).slug
        perm = Permission.objects.get(codename='change_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('edit_author', args=[slug]))
        self.assertTemplateUsed(response, 'catalog/authors/edit_author.html')

    '''
        url = 'author/<slug:slug>/delete'
    '''
    def test_delete_author_url_exists_at_desired_location_anonymous_user(self):
        slug = Author.objects.get(first_name=AUTHOR_FIRST_NAME).slug
        response = self.guest_client.get(reverse('delete_author', args=[slug]))
        self.assertEqual(response.status_code, 302)
    
    def test_delete_author_url_exists_at_desired_location_authorized_user_without_perms(self):
        slug = Author.objects.get(first_name=AUTHOR_FIRST_NAME).slug
        response = self.authorized_client.get(reverse('delete_author', args=[slug]))
        self.assertEqual(response.status_code, 403)
    
    def test_delete_author_url_exists_at_desired_location_authorized_user_with_perms(self):
        slug = Author.objects.get(first_name=AUTHOR_FIRST_NAME).slug
        perm = Permission.objects.get(codename='delete_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('delete_author', args=[slug]))
        self.assertEqual(response.status_code, 200)

    def test_delete_author_url_uses_correct_template(self):
        slug = Author.objects.get(first_name=AUTHOR_FIRST_NAME).slug
        perm = Permission.objects.get(codename='delete_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('delete_author', args=[slug]))
        self.assertTemplateUsed(response, 'catalog/authors/author_confirm_delete.html')

    '''
        url = '/books/'
    '''
    def test_books_url_exists_at_desired_location(self):
        response = self.guest_client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
    
    def test_books_url_uses_correct_template(self):
        response = self.guest_client.get(reverse('books'))
        self.assertTemplateUsed(response, 'catalog/books/book_list.html')

    '''
        url = '/books/add_book'
    '''
    def test_add_book_url_exists_at_desired_location_anonymous_user(self):
        response = self.guest_client.get(reverse('add_book'))
        self.assertEqual(response.status_code, 302)
    
    def test_add_book_url_exists_at_desired_location_authorized_user_without_perms(self):
        response = self.authorized_client.get(reverse('add_book'))
        self.assertEqual(response.status_code, 403)
    
    def test_add_book_url_exists_at_desired_location_authorized_user_with_perms(self):
        perm = Permission.objects.get(codename='add_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('add_book'))
        self.assertEqual(response.status_code, 200)

    def test_add_book_url_uses_correct_template(self):
        perm = Permission.objects.get(codename='add_book')    
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('add_book'))
        self.assertTemplateUsed(response, 'catalog/books/add_book.html')
    
    '''
        url = '/books/add_genre'
    '''
    def test_add_genre_url_exists_at_desired_location_anonymous_user(self):
        response = self.guest_client.get(reverse('add_genre'))
        self.assertEqual(response.status_code, 302)
    
    def test_add_genre_url_exists_at_desired_location_authorized_user_without_perms(self):
        response = self.authorized_client.get(reverse('add_genre'))
        self.assertEqual(response.status_code, 403)
    
    def test_add_genre_url_exists_at_desired_location_authorized_user_with_perms(self):
        perm = Permission.objects.get(codename='add_genre')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('add_genre'))
        self.assertEqual(response.status_code, 200)

    def test_add_genre_url_uses_correct_template(self):
        perm = Permission.objects.get(codename='add_genre')    
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('add_genre'))
        self.assertTemplateUsed(response, 'catalog/books/add_genre.html')

    '''
        book = 'book/<slug:slug>'
    '''
    def test_book_url_exists_at_desired_location(self):
        slug = Book.objects.get(title=BOOK_TITLE).slug
        response = self.guest_client.get(reverse('book_detail', args=[slug]))
        self.assertEqual(response.status_code, 200)
    
    def test_book_url_uses_correct_template(self):
        slug = Book.objects.get(title=BOOK_TITLE).slug
        response = self.guest_client.get(reverse('book_detail', args=[slug]))
        self.assertTemplateUsed(response, 'catalog/books/book_detail.html')

    '''
        url = 'book/<slug:slug>/edit'
    '''
    def test_edit_book_url_exists_at_desired_location_anonymous_user(self):
        slug = Book.objects.get(title=BOOK_TITLE).slug
        response = self.guest_client.get(reverse('edit_book', args=[slug]))
        self.assertEqual(response.status_code, 302)
    
    def test_edit_book_url_exists_at_desired_location_authorized_user_without_perms(self):
        slug = Book.objects.get(title=BOOK_TITLE).slug
        response = self.authorized_client.get(reverse('edit_book', args=[slug]))
        self.assertEqual(response.status_code, 403)
    
    def test_edit_book_url_exists_at_desired_location_authorized_user_with_perms(self):
        slug = Book.objects.get(title=BOOK_TITLE).slug
        perm = Permission.objects.get(codename='change_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('edit_book', args=[slug]))
        self.assertEqual(response.status_code, 200)

    def test_edit_book_url_uses_correct_template(self):
        slug = Book.objects.get(title=BOOK_TITLE).slug
        perm = Permission.objects.get(codename='change_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('edit_book', args=[slug]))
        self.assertTemplateUsed(response, 'catalog/books/edit_book.html')
    
    '''
        url = 'book/<slug:delete>/edit'
    '''
    def test_delete_book_url_exists_at_desired_location_anonymous_user(self):
        slug = Book.objects.get(title=BOOK_TITLE).slug
        response = self.guest_client.get(reverse('delete_book', args=[slug]))
        self.assertEqual(response.status_code, 302)
    
    def test_delete_book_url_exists_at_desired_location_authorized_user_without_perms(self):
        slug = Book.objects.get(title=BOOK_TITLE).slug
        response = self.authorized_client.get(reverse('delete_book', args=[slug]))
        self.assertEqual(response.status_code, 403)
    
    def test_delete_book_url_exists_at_desired_location_authorized_user_with_perms(self):
        slug = Book.objects.get(title=BOOK_TITLE).slug
        perm = Permission.objects.get(codename='delete_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('delete_book', args=[slug]))
        self.assertEqual(response.status_code, 200)

    def test_delete_book_url_uses_correct_template(self):
        slug = Book.objects.get(title=BOOK_TITLE).slug
        perm = Permission.objects.get(codename='delete_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('delete_book', args=[slug]))
        self.assertTemplateUsed(response, 'catalog/books/book_confirm_delete.html')
    
    
    '''
        url = 'bookshelf/'
    '''
    def test_bookshelf_url_exists_at_desired_location_anonymous_user(self):
        response = self.guest_client.get(reverse('bookshelf'))
        self.assertEqual(response.status_code, 302)
    
    def test_bookshelf_url_exists_at_desired_location_anonymous_user_url_exists_at_desired_location_authorized_user_with_perms(self):
        response = self.authorized_client.get(reverse('bookshelf'))
        self.assertEqual(response.status_code, 200)
    
    def test_bookshelf_book_url_uses_correct_template(self):
        response = self.authorized_client.get(reverse('bookshelf'))
        self.assertTemplateUsed(response, 'catalog/bookshelf/bookshelf.html')