from rest_framework import serializers
from .models import GenericArticle


class GenericArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    author_id = serializers.IntegerField()

    class Meta:
        model = GenericArticle
        fields = ('id', 'title', 'description', 'body', 'author_id')


