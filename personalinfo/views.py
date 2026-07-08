from django.shortcuts import render
from .models import PersonalInformation

def personal_info_page(request):
    personal_info = PersonalInformation.objects.all()
    return render(request, "personal-info/personal_info.html", {"personal_info": personal_info})


# Create your views here.
