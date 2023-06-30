from rest_framework import serializers
from rareapi.models.subscription import Subscription
from .rare_user_serializer import RareUserSerializer, UserPostSerializer

class SubscriptionSerializer(serializers.ModelSerializer):
    """JSON serializer for subscriptions
    """
    author_id = RareUserSerializer()
    posts = UserPostSerializer(many=True, read_only=True, source='author_id.posts')
    class Meta:
        model = Subscription
        fields = ('id', 'follower_id', 'author_id',
                  'created_on', 'ended_on', 'posts')
        depth = 1
