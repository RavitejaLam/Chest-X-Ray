import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
# Create your views here.

from django.views import View
from django.views.generic import CreateView
from .models import *
from .forms import *

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


class CreateTestingView(CreateView):
    model = Testing
    form_class = TestingForm
    template_name = 'chestxray.html'

    def get_context_data(self, **kwargs):
        context = super(CreateTestingView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        test_form = TestingForm(request.POST,request.FILES)
            # import ipdb
            # ipdb.set_trace()
        if test_form.is_valid() and request.FILES:
            test = test_form.save(commit=False)
            test.submitted_on = datetime.date.today()
            test.user = self.request.user
            test.image = request.FILES['myfile']
            test.save()
        return redirect('chestxray:home')

def result(request):
    # import ipdb
    # ipdb.set_trace()
    context_dict = {}
    test_result = Testing.objects.filter(user = request.user)
    context_dict['result'] = test_result
    # try:
    #     profile = Profile.objects.get(user = request.user)
    #     context_dict['prof'] = profile
    # except:
    #     pass
    return render(request, 'history.html', context_dict)