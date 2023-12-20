from django.test import TestCase

from Catalog.forms import *

class AddBookFormTest(TestCase):
    
    def setUp(self):
        self.form = AddBookForm()
    
    def test_title_field_label(self):
        self.assertEqual(self.form.fields['title'].label, "Название")
    
    def test_author_field_label(self):
        self.assertEqual(self.form.fields['author'].label, "Автор")
    
    def test_genre_field_label(self):
        self.assertEqual(self.form.fields['genre'].label, "Жанр")
    
    def test_about_field_label(self):
        self.assertEqual(self.form.fields['about'].label, "Описание книги")
    
    def test_link_to_file_field_label(self):
        self.assertEqual(self.form.fields['link_to_file'].label, "Путь до файла")
    
    def test_image_field_label(self):
        self.assertEqual(self.form.fields['image'].label, "Изображение")