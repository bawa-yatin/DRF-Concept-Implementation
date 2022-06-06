from django.shortcuts import render
from .models import Contact, User


# Create your views here.

def show_users(request):
    user = User.objects.get(username="Aniket Sinha")
    contact_list = user.contacts.all()
    contact_item = Contact.objects.get(email="john@john.dev")
    user_list = contact_item.user

    context = {"details": user, "contact_list": contact_list, "user_list": user_list}

    return render(request, 'user_list.html', context)
