from django.urls import path
from .views import testimony_create_view, TestimonyListView

urlpatterns = [
    path('create/', testimony_create_view, name='testimony_create'),
    path('list/', TestimonyListView.as_view(), name='testimony_list'),
]
