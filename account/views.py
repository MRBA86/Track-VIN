from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render , redirect
from django.views import View
from .forms import UserRegistrationForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout




class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/Register.html'

    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated:
            return redirect('account:user_profile')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        form = self.form_class()
        return render ( request, self.template_name , {'form' : form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            user.save()
            messages.success(request, 'ثبت نام با موفقیت انجام شد','success')
            return redirect('home:home')
        return render ( request, self.template_name , {'form' : form})

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'home/home.html'

    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated:
            return redirect('account:user_profile')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name , {'form' : form})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username= cd['username'], password=cd['password'])
            if user is not None :
                login(request, user)
                messages.success(request, 'ورود با موفقیت انجام شد', 'success')
                return redirect('account:user_profile')
            messages.error(request,'ورود نا موفق', 'warning')
        return render(request, self.template_name , {'form' : form})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'خروج کاربر با موفقیت انجام شد', 'success')
        return redirect('home:home')

            

class UserProfileView(View):
    def get(self, request):
        return render(request, 'account/Profile.html')         