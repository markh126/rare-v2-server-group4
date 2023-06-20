from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment, Post
from rareapi.serializers import CommentSerializer

class CommentView(ViewSet):
    """Rare comments view"""
    def update(self, request, pk):
      """Handle PUT requests for a comment
      
      Returns: 
          Response - empty body with 204 
          status code
      """
      comment = Comment.objects.get(pk=pk)
      comment.content = request.data["content"]
      comment.save()
      
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk):
      """Handle GET request for single comment
      
      Returns: 
          Response -- JSON serialized comment
      """
      try:
          comment = Comment.objects.get(pk=pk)
          serializer = CommentSerializer(comment)
          return Response(serializer.data)
      except Comment.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.
          HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk):
      """Handle DELETE requests for single comment
      
      Returns: 
          Response -- empty body with 204 status code
      """
      comment = Comment.objects.get(pk=pk)
      comment.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
