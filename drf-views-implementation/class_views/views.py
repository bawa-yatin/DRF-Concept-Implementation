from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Article, Author
from .serializers import ArticleSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.

class ArticleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is not None:
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article)
            return Response({'success': 'success', "students": serializer.data}, status=200)

        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'status': 'success', "articles": serializer.data}, status=200)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(saved_article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def patch(self, request, pk):
        saved_article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(saved_article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        result = get_object_or_404(Article, id=id)
        result.delete()
        return Response({"status": "success", "data": "Record Deleted"})
