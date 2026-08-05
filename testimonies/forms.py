from django import forms
from .models import Testimony

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'content']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your testimony'}),
        }
