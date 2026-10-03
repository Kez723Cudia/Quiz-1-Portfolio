from django import forms
from .models import Project, TechStack

class ProjectForm(forms.ModelForm):
    tech_stacks = forms.ModelMultipleChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Tech Stacks",
    )
    
    
    class Meta:
        model = Project
        fields = [
            "project_name",
            "description",
            "tech_stacks",
            "link",
        ]

        widgets = {
            "project_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),
            "link": forms.URLInput(
                attrs={"class": "form-control"}
            ),
        }

class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter tech stack name",
                }
            ),
        }
