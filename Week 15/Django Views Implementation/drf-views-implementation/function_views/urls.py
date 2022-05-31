from .views import students_list, students_details
from django.urls import path

urlpatterns = [
    path('student/', students_list),
    path('student/<int:pk>/', students_details)
]
