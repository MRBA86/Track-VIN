from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput )
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        cd = self.cleaned_data
        user = User.objects.filter(username=cd['username']).exists()
        if user :
            raise ValidationError('نام کاربری قبلا ثبت نام شده است')
        return cd

    def clean_email(self):
        cd = self.cleaned_data
        user = User.objects.filter(email=cd['email']).exists()
        if user :
            raise ValidationError('آدرس ایمیل قبلا استفاده شده است')
        return cd