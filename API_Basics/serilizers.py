from curses import meta
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    class Meta:
        model=Article
        field=['id', 'title', 'author']