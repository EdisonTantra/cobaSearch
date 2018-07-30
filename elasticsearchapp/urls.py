from django.conf.urls import url, include
from django.contrib import admin
from .views import searchDiseases, index, setup

urlpatterns = [
    url(r'^$', index),
    url(r'^search', searchDiseases),
    url(r'^setup', setup)
]