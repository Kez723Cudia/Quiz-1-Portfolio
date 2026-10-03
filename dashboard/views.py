from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from projects.models import Project, TechStack
from projects.forms import TechStackForm


def superuser_sign_in(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("dashboard_home")

        logout(request)

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is None:
            messages.error(
                request,
                "Invalid username or password."
            )

        elif not user.is_superuser:
            messages.error(
                request,
                "Access denied. Only a superuser may sign in to the dashboard."
            )

        else:
            login(request, user)
            return redirect("dashboard_home")

    return render(request, "dashboard/sign_in.html")


def dashboard_home(request):
    if not request.user.is_authenticated:
        return redirect("dashboard_sign_in")

    if not request.user.is_superuser:
        logout(request)
        messages.error(
            request,
            "Access denied. Only a superuser may access the dashboard."
        )
        return redirect("dashboard_sign_in")

    projects = Project.objects.all()
    tech_stacks = TechStack.objects.all()

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "projects": projects,
            "tech_stacks": tech_stacks,
        }
    )


def techstack_create_view(request):
    if not request.user.is_authenticated:
        return redirect("dashboard_sign_in")

    if not request.user.is_superuser:
        logout(request)
        return redirect("dashboard_sign_in")

    form = TechStackForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(
            request,
            "Tech stack created successfully."
        )
        return redirect("dashboard_home")

    return render(
        request,
        "dashboard/techstack_create.html",
        {
            "form": form,
        }
    )

@require_POST
def dashboard_logout(request):
    logout(request)
    messages.success(request, "You have signed out successfully.")
    return redirect("dashboard_sign_in")