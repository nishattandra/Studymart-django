from django.shortcuts import render
from django.http import HttpResponse

def machine(request):
    return HttpResponse("Welcome to django practice")
