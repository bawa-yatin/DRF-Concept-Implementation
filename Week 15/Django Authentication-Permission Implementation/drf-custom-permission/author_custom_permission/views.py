from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from .permissions import StaffAllButEditOrReadOnly


# Create your views here.
class ArticleView(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [StaffAllButEditOrReadOnly]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
