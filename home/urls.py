from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_page, name='home'),
]


