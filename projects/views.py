from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.contrib.auth import logout

# Dynamic views for Quiz 2
def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/list.html", {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "projects/detail.html", {'project': project})

# Function-based view: Create project
def project_create_view(request):
    if not request.user.is_authenticated:
        return redirect("dashboard_sign_in")
    if not request.user.is_superuser:
        logout(request)
        messages.error(
            request,
            "Access denied. Only a superuser may access the dashboard."
        )
        return redirect("dashboard_sign_in")
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(
            request,
            "Project created successfully."
        )
        return redirect("project_list")
    
    return render(
        request,
        "projects/create.html",
        {
            "form": form,
        }
    )


# Create your views here.
