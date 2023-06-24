from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, RareUser, Comment
from rareapi.serializers import PostSerializer, CommentSerializer
from django.db import models
from rest_framework.decorators import action


class PostView(ViewSet):
  
    def retrieve(self, request, pk):
      
        post= Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        data = serializer.data
        
        return Response(data)

    def list(self,request):
         
         posts = Post.objects.all()
         user = request.query_params.get('user')
         posts = posts.filter(user_id = user)
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
        post.image_url = request.data.get("imageUrl", post.image_url)
        post.content = request.data.get("content", post.content)
        
        post.save()
        
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
      post = Post.objects.get(pk=pk)
      post.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
  
    @action(methods=['post'], detail=True)
    def post_comment(self, request, pk):
        """Post request for a user to post a comment"""
        author_id = RareUser.objects.get(pk=request.data["authorId"])
        post_id = Post.objects.get(pk=pk)
        new_comment = Comment.objects.create(
            author_id=author_id,
            post_id=post_id,
            content=request.data["content"]
        )
        return Response({'message': 'Comment posted'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['get'], detail=True)
    def comments(self, request, pk):
        """Get request for a user to see all 
        comments for a post"""
        comments = Comment.objects.all()
        post_comments = comments.filter(post_id=pk)
        
        serializer = CommentSerializer(post_comments, many=True)
        return Response(serializer.data)
        
        
