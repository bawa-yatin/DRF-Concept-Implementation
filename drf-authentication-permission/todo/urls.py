from django.urls import path
from .views import TodoList, CreateTodo, SingleTodo

urlpatterns = [
   path('all-items/', TodoList.as_view()),
   path('create-item/', CreateTodo.as_view()),
   path('item/<int:pk>/', SingleTodo.as_view())
]