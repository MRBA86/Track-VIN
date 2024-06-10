from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.http import HttpResponse


class HomeView(View):
    def get(self,request):
        return render (request, 'home/home.html')

# Create your views here.

