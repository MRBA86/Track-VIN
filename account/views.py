from django.shortcuts import render , redirect
from django.views import View
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages





class RegisterView(View):
    form_class = UserRegistrationForm
    template_class = 'account/Register.html'

    def get(self,request):
        form = self.form_class()
        return render ( request, self.template_class , {'form' : form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.save()
            messages.success(request, 'username created successfully','success')
            return redirect('home:home')
        return render ( request, self.template_class , {'form' : form})
