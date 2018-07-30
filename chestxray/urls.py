from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from chestxray.views import *

app_name="chestxray"

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('about/',AboutView.as_view(),name="about"),
    path('models/',ModelsView.as_view(),name="models"),
    path('team/',TeamView.as_view(),name="team"),
    path('contact/',ContactView.as_view(),name="contact"),
    path('gauth/',GauthView.as_view(),name="gauth"),
    path('chestxray/',CreateTestingView.as_view(),name="chestxray"),
    url(r'~/account/logout/?next=/', LogoutView.as_view(), name="logout"),
    url('log/',result,name="log"),
]