from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, RareUser
from rareapi.serializers import PostSerializer
from django.db import models


class PostView(ViewSet):
  
    def retrieve(self, request, pk):
      
        post= Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        data = serializer.data
        
        return Response(data)

    def list(self,request):
         
         posts = Post.objects.all()
         serializer = PostSerializer(posts, many=True)
         return Response(serializer.data)
 
    def create(self, request):
        user_id = RareUser.objects.get(pk=request.data["userId"])
        
        post =Post(
          title=request.data["title"],
          image_url=request.data["imageUrl"],
          content=request.data["content"],
          user_id=user_id,
        )
        
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        post = Post.objects.filter(pk=pk).first()
        post.title = request.data.get("title", post.title)
        post.image_url = request.data.get("image_url", post.image_url)
        post.content = request.data.get("content", post.content)
        
        post.save()
        
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
      post = Post.objects.get(pk=pk)
      post.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
