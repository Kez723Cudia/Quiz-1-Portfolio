from django.shortcuts import render
from .forms import TestimonyForm
from .models import Testimony
from django.views.generic import ListView

def testimony_create_view(request):
    form = TestimonyForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'testimonies/create.html', context)

class TestimonyListView(ListView):
    model = Testimony
    template_name = 'testimonies/list.html'
    context_object_name = 'testimonies'

# Create your views here.
