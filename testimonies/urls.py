from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.testimony_create_view, name='testimony_create'),
    path('list/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('<int:pk>/', views.testimony_detail, name='testimony_detail'),
]
