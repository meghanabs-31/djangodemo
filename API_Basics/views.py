from pickle import FALSE, GET
from telnetlib import STATUS
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from requests import post
from rest_framework.parsers import JSONParser
from yaml import serializer
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
def article_list(request):

    if request.method == GET :
        articles = Article.objects.all()
        serializer = ArticleSerializer (articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == post:
        data = JSONParser().parser(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, STATUS=201)
        return JsonResponse(serializer.errors, status=400)




        
