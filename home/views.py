from django.shortcuts import render

def hero_page(request):
    return render(request, 'home/hero.html')

# Create your views here.
