from django.urls import path, include
from rest_framework import routers
from .views import CartItemViews

router = routers.DefaultRouter()
router.register(r'item', CartItemViews)

urlpatterns = [
    path('', include(router.urls))
]