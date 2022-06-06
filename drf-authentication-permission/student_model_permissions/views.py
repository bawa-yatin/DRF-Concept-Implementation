from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions


# Create your views here.
class StudentView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
