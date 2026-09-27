from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InquiryForm

def inquiry_create_view(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inquiry submitted successfully. Engr. Cudia will respond shortly. Thank you for getting in touch!")
            return redirect('contact')
    else:
        form = InquiryForm()
    context = {'form': form}
    return render(request, "contact/contact.html", context)

# Create your views here.
