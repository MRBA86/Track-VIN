from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponse


class HomeView(View):

    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated:
            return redirect('account:user_profile')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        return render (request, 'home/home.html')

# Create your views here.

