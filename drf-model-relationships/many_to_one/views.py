from django.shortcuts import render
from .models import Contact, User


# Create your views here.

# View function for displaying the list of users along with their contact info
def show_users(request):
    # Fetching user contact details
    user = User.objects.get(username="Aniket Sinha")
    contact_list = user.contacts.all()

    # Fetching user from their contact details
    contact_item = Contact.objects.get(email="john@john.dev")
    user_list = contact_item.user

    context = {"details": user, "contact_list": contact_list, "user_list": user_list}

    # Passing the fetched results onto a HTML template
    return render(request, 'user_list.html', context)
