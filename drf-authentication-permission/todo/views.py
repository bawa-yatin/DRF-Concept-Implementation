from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

class CreateTodo(CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoList(ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Todo.objects.all().filter(completed=True)
    serializer_class = TodoSerializer


class SingleTodo(RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
