from django.shortcuts import render
from .forms import InquiryForm

def inquiry_create_view(request):
    form = InquiryForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, "contact/contact.html", context)

# Create your views here.
