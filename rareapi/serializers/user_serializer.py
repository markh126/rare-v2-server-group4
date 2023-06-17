from rest_framework import serializers
from rareapi.models.user import User

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ('id',
                  'uid',
                  'first_name',
                  'last_name',
                  'email',
                  'username',
                  'password',
                  'is_staff')
