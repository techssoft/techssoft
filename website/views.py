from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and phone and message:
            Contact.objects.create(
                name=name,
                phone=phone,
                email=email,
                message=message
            )
            messages.success(request, 'Thank you for contacting us!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill all required fields.')
    return render(request, 'website/contact.html')


def careers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and phone and message:
            Contact.objects.create(
                name=name,
                phone=phone,
                email=email,
                message=message
            )
            messages.success(request, 'Thank you for contacting us!')
            return redirect('careers')
        else:
            messages.error(request, 'Please fill all required fields.')
    return render(request, 'website/careers.html')

def services(request):
    return render(request, 'website/services.html')

def industries(request):
    return render(request, 'website/industries.html')

def login_view(request):
    return render(request, 'website/login.html')

def artificial_intelligence(request):
    return render(request, 'website/artificial_intelligence.html')

def cyber_security(request):
    return render(request, 'website/cyber_security.html')

def data_science(request):
    return render(request, 'website/data_science.html')

def application_development(request):
    return render(request, 'website/Application_development.html')

def website_development(request):
    return render(request, 'website/website_development.html')

def software_development(request):
    return render(request, 'website/software_development.html')
