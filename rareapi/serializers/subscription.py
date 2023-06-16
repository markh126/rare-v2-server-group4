from rest_framework import serializers
from models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    """JSON serializer for subscriptions
    """
    class Meta:
        model = Subscription
        fields = ('id', 'follower_id', 'author_id',
                  'created_on', 'ended_on')
        depth = 1
