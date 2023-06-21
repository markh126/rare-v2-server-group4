from rest_framework import serializers
from rareapi.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = Comment
        fields = ('content', 'author_id', 'post_id', 'created_on')
        depth = 0
