from django.urls import path
from . import views

urlpatterns = [
    path(
        "sign-in/",
        views.superuser_sign_in,
        name="dashboard_sign_in",
    ),
    path(
        "dashboard/",
        views.dashboard_home,
        name="dashboard_home",
    ),
    path(
        "dashboard/tech-stacks/create/",
        views.techstack_create_view,
        name="techstack_create",
    ),
    path(
        "dashboard/logout/",
        views.dashboard_logout,
        name="dashboard_logout",
    ),
]
