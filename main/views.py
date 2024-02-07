from django.shortcuts import render
from .models import ClientData
from django.contrib import messages

# Create your views here.

def landingPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Check if the email already exists
        if ClientData.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please use a different email.')
        else:
            # Save the form data to the database
            client_data = ClientData(name=name, email=email)
            client_data.save()

            # Show success message
            messages.success(request, 'Form submitted successfully!')

        # Save data to the database
        # client_data = ClientData(name=name, email=email)
        # client_data.save()

    return render(request, 'index.html')