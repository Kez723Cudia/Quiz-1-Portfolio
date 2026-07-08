from django.shortcuts import render, get_object_or_404
from .models import Project

# Dynamic views for Quiz 2
def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/list.html", {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "projects/detail.html", {'project': project})

# Create your views here.
