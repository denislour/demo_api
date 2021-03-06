from django.http import JsonResponse, request
from django.shortcuts import render
from rest_framework import serializers

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import PostSerializers
from .models import Post


class TestView(APIView):

    def get(self, request):
        data = {
            'name': 'Son',
            'age': 28,
        }
        return Response(data)


class PostView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PostViewDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializers(post)
        return Response(serializer.data)

    def put(self, request, pk): 
        post = Post.objects.get(pk=pk)
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({'message': 'Deleted post'})

# def test_view(request):
#     data = {  
#         'name': 'Son',
#         'age': '28',
#     }
#     return JsonResponse(data)
