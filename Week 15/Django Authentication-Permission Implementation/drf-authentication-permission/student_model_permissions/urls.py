from django.urls import path, include
from rest_framework import routers
from .views import StudentView

router = routers.DefaultRouter()
router.register(r'stu', StudentView)

urlpatterns = [
    path('', include(router.urls))
]