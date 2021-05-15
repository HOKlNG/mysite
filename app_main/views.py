from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.generic.edit import FormView, View


# Create your views here.


def index(request):
    return render(request, 'index.html')
