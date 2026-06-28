from django.shortcuts import render
from django.http import HttpResponse

def hero_page(request):
    return HttpResponse("<h1>Kezia Cudia</h1><p>Beginner Django Developer | Open for Opportunities</p>")

# Create your views here.
