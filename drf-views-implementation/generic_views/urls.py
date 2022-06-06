from django.urls import path
from .views import GenericArticleView, SingleArticleView

urlpatterns = [
    path('articles/', GenericArticleView.as_view()),
    path('articles/<int:pk>/', SingleArticleView.as_view())
]