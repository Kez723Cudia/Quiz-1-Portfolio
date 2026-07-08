from django.urls import path
from . import views

urlpatterns = [
    path('', views.personal_info_page, name='personal_info'),
]
