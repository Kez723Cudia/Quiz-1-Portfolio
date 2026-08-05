from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stack', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tech_stack': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
        }
