from rest_framework import serializers
from rareapi.models.rare_user import RareUser
from rareapi.models.post import Post

class UserPostSerializer(serializers.ModelSerializer):
    """json serializer for showing user posts"""
   
    class Meta:
        model = Post
        fields = ('id',
                  'user_id',
                  'title',
                  'publication_date',
                  'image_url',
                  'content')
    

class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for rare users"""
    subscription_count = serializers.IntegerField(default=None)
    posts = UserPostSerializer(many=True, read_only=True, source='user')
    class Meta:
        model = RareUser
        fields = ('id',
                  'first_name',
                  'last_name',
                  'bio',
                  'profile_image_url',
                  'email',
                  'created_on',
                  'active',
                  'is_staff',
                  'subscription_count',
                  'uid',
                  'posts')


class CreateRareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for creating rare users"""
    class Meta:
        model = RareUser
        fields = ('id',
                  'first_name',
                  'last_name',
                  'bio',
                  'profile_image_url',
                  'email',
                  'active')
