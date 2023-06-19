from rest_framework import serializers
from rareapi.models.rare_user import RareUser

class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for rare users"""
    subscription_count = serializers.IntegerField(default=None)
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
                  'uid')

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