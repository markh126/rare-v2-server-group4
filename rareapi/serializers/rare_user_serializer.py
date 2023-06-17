from rest_framework import serializers
from rareapi.models.rare_user import RareUser

class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for rare users"""
    class Meta:
        model = RareUser
        fields = ('id',
                  'bio',
                  'profile_image_url',
                  'created_on',
                  'active',
                  'user_id')

class CreateRareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for creating rare users"""
    class Meta:
        model = RareUser
        fields = ('id',
                  'bio',
                  'profile_image_url',
                  'active')