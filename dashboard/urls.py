from django.urls import path
from . import views

urlpatterns = [
    path("sign-in/", views.superuser_sign_in, name="dashboard_sign_in"),
    path("dashboard/", views.dashboard_home, name="dashboard_home"),
    path("dashboard/logout/", views.dashboard_logout, name="dashboard_logout"),
]