from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
class EmpCRUD(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
