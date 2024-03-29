from django.test import TestCase, Client
from django.contrib.auth.models import Permission

from Catalog.views import *


class TestUrl(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        Genre.objects.create(
            genre="genre_name"
        )
        author = Author.objects.create(
            first_name='Имя_тест',
            last_name='Фамилия_тест',
            date_of_birth='1998-03-03'
        )
        book = Book.objects.create(
            title='Тестовая_книга',
            author=author
        )
        book.genre.set(Genre.objects.all())

    def setUp(self):
        self.guest_client = Client()

        self.user = get_user_model().objects.create(username="client_user")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    # url = '/'
    def test_index_url_exists_at_desired_location(self):
        response = self.guest_client.get(reverse('catalog:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_url_uses_correct_template(self):
        response = self.guest_client.get(reverse('catalog:index'))
        self.assertTemplateUsed(response, 'catalog/index.html')

    # url = '/authors/'
    def test_authors_url_exists_at_desired_location(self):
        response = self.guest_client.get(reverse('catalog:authors'))
        self.assertEqual(response.status_code, 200)

    def test_authors_url_uses_correct_template(self):
        response = self.guest_client.get(reverse('catalog:authors'))
        self.assertTemplateUsed(response, 'catalog/authors/author_list.html')

    # url = '/authors/add_author/'
    def test_add_author_url_exists_at_desired_location_anonymous_user(self):
        response = self.guest_client.get(reverse('catalog:add_author'))
        self.assertEqual(response.status_code, 302)

    def test_add_author_url_exists_at_desired_location_authorized_user_without_perms(self):
        response = self.authorized_client.get(reverse('catalog:add_author'))
        self.assertEqual(response.status_code, 403)

    def test_add_author_url_exists_at_desired_location_authorized_user_with_perms(self):
        perm = Permission.objects.get(codename='add_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('catalog:add_author'))
        self.assertEqual(response.status_code, 200)

    def test_add_author_url_uses_correct_template(self):
        perm = Permission.objects.get(codename='add_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('catalog:add_author'))
        self.assertTemplateUsed(response, 'catalog/authors/add_author.html')

    # url = 'author/<slug:slug>'
    def test_author_url_exists_at_desired_location(self):
        slug = Author.objects.get(first_name='Имя_тест').slug
        response = self.guest_client.get(reverse('catalog:author_detail', args=[slug]))
        self.assertEqual(response.status_code, 200)

    def test_author_url_uses_correct_template(self):
        slug = Author.objects.get(first_name='Имя_тест').slug
        response = self.guest_client.get(reverse('catalog:author_detail', args=[slug]))
        self.assertTemplateUsed(response, 'catalog/authors/author_detail.html')

    # url = 'author/<slug:slug>/edit'
    def test_edit_author_url_exists_at_desired_location_anonymous_user(self):
        slug = Author.objects.get(first_name='Имя_тест').slug
        response = self.guest_client.get(reverse('catalog:edit_author', args=[slug]))
        self.assertEqual(response.status_code, 302)

    def test_edit_author_url_exists_at_desired_location_authorized_user_without_perms(self):
        slug = Author.objects.get(first_name='Имя_тест').slug
        response = self.authorized_client.get(
            reverse('catalog:edit_author', args=[slug]))
        self.assertEqual(response.status_code, 403)

    def test_edit_author_url_exists_at_desired_location_authorized_user_with_perms(self):
        slug = Author.objects.get(first_name='Имя_тест').slug
        perm = Permission.objects.get(codename='change_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(
            reverse('catalog:edit_author', args=[slug]))
        self.assertEqual(response.status_code, 200)

    def test_edit_author_url_uses_correct_template(self):
        slug = Author.objects.get(first_name='Имя_тест').slug
        perm = Permission.objects.get(codename='change_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(
            reverse('catalog:edit_author', args=[slug]))
        self.assertTemplateUsed(response, 'catalog/authors/edit_author.html')

    # url = 'author/<slug:slug>/delete'
    def test_delete_author_url_exists_at_desired_location_anonymous_user(self):
        slug = Author.objects.get(first_name='Имя_тест').slug
        response = self.guest_client.get(reverse('catalog:delete_author', args=[slug]))
        self.assertEqual(response.status_code, 302)

    def test_delete_author_url_exists_at_desired_location_authorized_user_without_perms(self):
        slug = Author.objects.get(first_name='Имя_тест').slug
        response = self.authorized_client.get(
            reverse('catalog:delete_author', args=[slug]))
        self.assertEqual(response.status_code, 403)

    def test_delete_author_url_exists_at_desired_location_authorized_user_with_perms(self):
        slug = Author.objects.get(first_name='Имя_тест').slug
        perm = Permission.objects.get(codename='delete_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(
            reverse('catalog:delete_author', args=[slug]))
        self.assertEqual(response.status_code, 200)

    def test_delete_author_url_uses_correct_template(self):
        slug = Author.objects.get(first_name='Имя_тест').slug
        perm = Permission.objects.get(codename='delete_author')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(
            reverse('catalog:delete_author', args=[slug]))
        self.assertTemplateUsed(
            response, 'catalog/authors/author_confirm_delete.html')

    # url = '/books/'
    def test_books_url_exists_at_desired_location(self):
        response = self.guest_client.get(reverse('catalog:books'))
        self.assertEqual(response.status_code, 200)

    def test_books_url_uses_correct_template(self):
        response = self.guest_client.get(reverse('catalog:books'))
        self.assertTemplateUsed(response, 'catalog/books/book_list.html')

    # url = '/books/add_book'
    def test_add_book_url_exists_at_desired_location_anonymous_user(self):
        response = self.guest_client.get(reverse('catalog:add_book'))
        self.assertEqual(response.status_code, 302)

    def test_add_book_url_exists_at_desired_location_authorized_user_without_perms(self):
        response = self.authorized_client.get(reverse('catalog:add_book'))
        self.assertEqual(response.status_code, 403)

    def test_add_book_url_exists_at_desired_location_authorized_user_with_perms(self):
        perm = Permission.objects.get(codename='add_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('catalog:add_book'))
        self.assertEqual(response.status_code, 200)

    def test_add_book_url_uses_correct_template(self):
        perm = Permission.objects.get(codename='add_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('catalog:add_book'))
        self.assertTemplateUsed(response, 'catalog/books/add_book.html')

    # url = '/books/add_genre'
    def test_add_genre_url_exists_at_desired_location_anonymous_user(self):
        response = self.guest_client.get(reverse('catalog:add_genre'))
        self.assertEqual(response.status_code, 302)

    def test_add_genre_url_exists_at_desired_location_authorized_user_without_perms(self):
        response = self.authorized_client.get(reverse('catalog:add_genre'))
        self.assertEqual(response.status_code, 403)

    def test_add_genre_url_exists_at_desired_location_authorized_user_with_perms(self):
        perm = Permission.objects.get(codename='add_genre')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('catalog:add_genre'))
        self.assertEqual(response.status_code, 200)

    def test_add_genre_url_uses_correct_template(self):
        perm = Permission.objects.get(codename='add_genre')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(reverse('catalog:add_genre'))
        self.assertTemplateUsed(response, 'catalog/books/add_genre.html')

    # url = 'book/<slug:slug>'
    def test_book_url_exists_at_desired_location(self):
        slug = Book.objects.get(title='Тестовая_книга').slug
        response = self.guest_client.get(reverse('catalog:book_detail', args=[slug]))
        self.assertEqual(response.status_code, 200)

    def test_book_url_uses_correct_template(self):
        slug = Book.objects.get(title='Тестовая_книга').slug
        response = self.guest_client.get(reverse('catalog:book_detail', args=[slug]))
        self.assertTemplateUsed(response, 'catalog/books/book_detail.html')

    # url = 'book/<slug:slug>/edit'
    def test_edit_book_url_exists_at_desired_location_anonymous_user(self):
        slug = Book.objects.get(title='Тестовая_книга').slug
        response = self.guest_client.get(reverse('catalog:edit_book', args=[slug]))
        self.assertEqual(response.status_code, 302)

    def test_edit_book_url_exists_at_desired_location_authorized_user_without_perms(self):
        slug = Book.objects.get(title='Тестовая_книга').slug
        response = self.authorized_client.get(
            reverse('catalog:edit_book', args=[slug]))
        self.assertEqual(response.status_code, 403)

    def test_edit_book_url_exists_at_desired_location_authorized_user_with_perms(self):
        slug = Book.objects.get(title='Тестовая_книга').slug
        perm = Permission.objects.get(codename='change_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(
            reverse('catalog:edit_book', args=[slug]))
        self.assertEqual(response.status_code, 200)

    def test_edit_book_url_uses_correct_template(self):
        slug = Book.objects.get(title='Тестовая_книга').slug
        perm = Permission.objects.get(codename='change_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(
            reverse('catalog:edit_book', args=[slug]))
        self.assertTemplateUsed(response, 'catalog/books/edit_book.html')

    # url = 'book/<slug:delete>/edit'
    def test_delete_book_url_exists_at_desired_location_anonymous_user(self):
        slug = Book.objects.get(title='Тестовая_книга').slug
        response = self.guest_client.get(reverse('catalog:delete_book', args=[slug]))
        self.assertEqual(response.status_code, 302)

    def test_delete_book_url_exists_at_desired_location_authorized_user_without_perms(self):
        slug = Book.objects.get(title='Тестовая_книга').slug
        response = self.authorized_client.get(
            reverse('catalog:delete_book', args=[slug]))
        self.assertEqual(response.status_code, 403)

    def test_delete_book_url_exists_at_desired_location_authorized_user_with_perms(self):
        slug = Book.objects.get(title='Тестовая_книга').slug
        perm = Permission.objects.get(codename='delete_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(
            reverse('catalog:delete_book', args=[slug]))
        self.assertEqual(response.status_code, 200)

    def test_delete_book_url_uses_correct_template(self):
        slug = Book.objects.get(title='Тестовая_книга').slug
        perm = Permission.objects.get(codename='delete_book')
        self.user.user_permissions.add(perm)
        response = self.authorized_client.get(
            reverse('catalog:delete_book', args=[slug]))
        self.assertTemplateUsed(
            response, 'catalog/books/book_confirm_delete.html')

    # url = 'bookshelf/'
    def test_bookshelf_url_exists_at_desired_location_anonymous_user(self):
        response = self.guest_client.get(reverse('catalog:bookshelf'))
        self.assertEqual(response.status_code, 302)

    def test_bookshelf_url_exists_at_desired_location_anonymous_user_url_exists_at_desired_location_authorized_user_with_perms(self):
        response = self.authorized_client.get(reverse('catalog:bookshelf'))
        self.assertEqual(response.status_code, 200)

    def test_bookshelf_book_url_uses_correct_template(self):
        response = self.authorized_client.get(reverse('catalog:bookshelf'))
        self.assertTemplateUsed(response, 'catalog/bookshelf/bookshelf.html')
