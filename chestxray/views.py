from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
# Create your views here.

from django.views import View

class HomeView(View):
    def get(self,request):
        return render(request,template_name="index.html")

class AboutView(View):
    def get(self,request):
        return render(request,template_name="about.html")
    
class ModelsView(View):
    def get(self,request):
        return render(request,template_name="models.html")

class TeamView(View):
    def get(self,request):
        return render(request,template_name="team.html")

class ContactView(View):
    def get(self,request):
        return render(request,template_name="contact.html")

class GauthView(View):
    def get(self,request):
        return render(request,template_name="gauth.html")

class ChestxrayView(View):
    def get(self,request):
        return render(request,template_name="chestxray.html")

class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')