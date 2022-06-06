from .views import StudentView, StudentIdView
from django.urls import path

urlpatterns = [
    path('basic/', StudentView.as_view()),
    path('basic/<int:id>/', StudentIdView.as_view())
]
