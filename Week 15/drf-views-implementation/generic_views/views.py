from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import GenericArticle, GenericAuthor
from .serializers import GenericArticleSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# Create your views here.
class GenericArticleView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = GenericArticle.objects.all()
    serializer_class = GenericArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(GenericAuthor, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = GenericArticle.objects.all()
    serializer_class = GenericArticleSerializer


