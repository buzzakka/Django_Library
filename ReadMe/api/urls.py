from django.urls import path, re_path
from . import views

app_name = "api"

urlpatterns = [
    path("books/", views.BookApiList.as_view()),
    path("book/<int:pk>", views.BookApiUpdate.as_view()),
]
