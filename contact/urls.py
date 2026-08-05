from django.urls import path
from .views import inquiry_create_view

urlpatterns = [
    path('', inquiry_create_view, name='contact'),
]

