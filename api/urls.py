from django.urls import path, include, re_path
from . import views

# app_name = "api"

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path("books/", views.BookApiList.as_view()),
    path("book/<int:pk>", views.BookApiUpdate.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
