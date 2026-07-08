from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInformation

# Existing static page view (from quiz 1)
def projects_page(request):
    return render(request, "projects/projects.html")

# Added views for Quiz 2
def list_view(request):
    projects = Project.objects.all()
    return render(request, "projects/list.html", {'projects': projects})

def detail_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "projects/detail.html", {'project': project})

def personal_info_view(request):
    personal_info = PersonalInformation.objects.all()
    return render(request, "projects/personal_info.html", {'personal_info': personal_info})

# Create your views here.
