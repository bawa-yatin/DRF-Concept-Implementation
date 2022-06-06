from django.shortcuts import render
from .models import Person, Aadhar


# Create your views here.

def aadhar_details(request):
    aadhar_item = Aadhar.objects.get(aadhar_no=891881917819)
    user_data = aadhar_item.person

    user_item = Person.objects.get(name="Kamal")
    aadharDetails = user_item.aadhar.aadhar_no

    return render(request, 'aadhar.html', {"user_data": user_data, "aadharDetails": aadharDetails})
