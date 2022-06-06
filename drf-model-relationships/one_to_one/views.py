from django.shortcuts import render
from .models import Person, Aadhar


# Create your views here.

# View function for displaying user's aadhar details
def aadhar_details(request):
    # Fetching user data on the basis of Aadhar no.
    aadhar_item = Aadhar.objects.get(aadhar_no=891881917819)
    user_data = aadhar_item.person

    # Fetching aadhar data on the basis of User Name
    user_item = Person.objects.get(name="Kamal")
    aadharDetails = user_item.aadhar.aadhar_no

    return render(request, 'aadhar.html', {"user_data": user_data, "aadharDetails": aadharDetails})
