from django.shortcuts import render
from .models import Sandwich, Sauce


# Create your views here.

# View function for rendering the home page
def homepage(request):
    return render(request, 'index.html')


# View function for displaying the list of sauces and sandwich based on a certain
# condition
def showlist(request):
    sandwich_item = Sandwich.objects.get(name="Chicken Teriyaki Sandwich")
    sauce_list = sandwich_item.sauces.all()

    bbq_sauce = Sauce.objects.get(name="Barbeque")
    # all() method to fetch all sandwiches that use "bbq_sauce"
    sandwich_list = bbq_sauce.sandwiches.all()
    # filter method to filter out sandwiches that use "mayonnaise"
    mayo_sandwich = Sandwich.objects.filter(sauces__id=2)

    return render(request, 'sauces.html', {"sauce_list": sauce_list, "sandwich_list": sandwich_list, "mayo_sandwich": mayo_sandwich})
