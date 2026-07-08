from django.urls import path
from . import views

urlpatterns = [
    # Quiz 1 static page
    path('', views.projects_page, name='projects'),

    # Quiz 2 dynamic views
    path('list/', views.list_view, name='project_list'),
    path('<int:project_id>/', views.detail_view, name='project_detail'),
    path('personal-info/', views.personal_info_view, name='personal_info'),
]
