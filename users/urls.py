from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.RegisterUser.as_view(), name="register"),

    path("profile/", views.ProfileUser.as_view(), name="profile"),
    path("profile/edit/", views.EditProfile.as_view(), name="edit-profile"),
    path("profile/change-password/", views.PasswordChange.as_view(), name="change-password"),
    path("profile/delete/", views.delete_user, name="delete"),
]
