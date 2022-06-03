from django.urls import path, include
from rest_framework import routers
from .views import EmpCRUD

router = routers.DefaultRouter()
router.register(r'emp', EmpCRUD)

urlpatterns = [
    path('', include(router.urls))
]