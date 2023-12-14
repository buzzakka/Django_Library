from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", required=True)
    email = forms.CharField(label="E-mail", required=True)
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(), required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким E-mail уже существует')
        return email


class EditProfileForm(UserChangeForm):
    image = forms.ImageField(label="Изображение")

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'image']
