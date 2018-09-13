from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class my_form(UserCreationForm):
    nickname = forms.CharField(required=True, max_length=50)
    birthday = forms.DateField(required=False)
    phonenumber = forms.CharField(required=True, max_length=12)
    #captcha = CaptchaField()
    class Meta:
        model = User
        fields = ('username', 'nickname', 'birthday', 'email', 'password1', 'password2')

class my_edit_form(UserChangeForm):
    nickname = forms.CharField(required=False, max_length=50)
    birthday = forms.DateField(required=False)
    phonenumber = forms.CharField(required=True, max_length=12)

    class Meta:
        model = User
        fields = ('username', 'nickname', 'birthday', 'email', 'password')

class my_login_form(AuthenticationForm):
    验证码 = forms.CharField(required=False, max_length=50)
     #captcha = CaptchaField()

