from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class EmpCRUD(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
