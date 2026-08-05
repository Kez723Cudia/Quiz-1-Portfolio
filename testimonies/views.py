from django.shortcuts import render, get_object_or_404, redirect
from .forms import TestimonyForm
from .models import Testimony
from django.views.generic import ListView

# Function-based view: Create testimony
def testimony_create_view(request):
    form = TestimonyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('testimony_create')  # Redirect to the same page after successful submission
    return render(request, 'testimonies/create.html', {'form': form})

# Class-based view: List testimonies
class TestimonyListView(ListView):
    model = Testimony
    template_name = 'testimonies/list.html'
    context_object_name = 'testimonies'

# Function-based view: Detail testimony
def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'testimonies/detail.html', {'testimony': testimony})

# Create your views here.
