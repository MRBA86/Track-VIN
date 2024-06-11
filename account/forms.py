from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='نام کاربری' , widget=forms.TextInput(attrs={'class': 'form-control col-md-3'}))
    email = forms.EmailField(label='پست الکترونیک', widget = forms.EmailInput(attrs={'class': 'form-control col-md-3'}) )
    password1 = forms.CharField(label='رمز عبور', widget = forms.PasswordInput(attrs={'class': 'form-control col-md-3'}))
    password2 = forms.CharField(label='تایید رمز عبور', widget = forms.PasswordInput(attrs={'class': 'form-control col-md-3'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user :
            raise ValidationError('نام کاربری قبلا ثبت نام شده است')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user :
            raise ValidationError('آدرس ایمیل قبلا استفاده شده است')
        return email
    
    def clean(self):
        cld = super().clean()
        p1 = cld.get("password1")
        p2 = cld.get("password2")
        if p1 and p2 and p1 != p2 :
            raise ValidationError('رمز عبور و تایید آن با هم یکسان نمی باشند')
        
class UserLoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری' , widget=forms.TextInput)
    password = forms.CharField(label='رمز عبور', widget = forms.PasswordInput)