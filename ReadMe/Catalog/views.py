from django.shortcuts import render
from django.http import HttpResponse
from .models import Author

# Create your views here.
def index(request):
    return HttpResponse("Privet")
