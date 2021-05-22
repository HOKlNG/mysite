from django.contrib import admin
from django.urls import path, include, re_path

from .views import index, blog, contact

urlpatterns = [
    path('',index),
    path('blog', blog),
    path('contact', contact),
]