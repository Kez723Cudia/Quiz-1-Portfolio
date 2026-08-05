from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.project_list, name='project_list'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create_view, name='project_create')
  
]
