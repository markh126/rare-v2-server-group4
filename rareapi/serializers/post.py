from rest_framework import serializers
from rareapi.models import Post

class PostSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Post
    fields = ('id', 'user_id', 'title', 'publication_date', 'image_url', 'content')
