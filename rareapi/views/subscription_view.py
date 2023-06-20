from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from rareapi.models.subscription import Subscription
from rareapi.serializers.subscription_serializer import SubscriptionSerializer
from rareapi.models.rare_user import RareUser

class SubscriptionView(ViewSet):
    """Subscription views
    """
    
    def retrieve(self, request, pk):
        """Handle GET requests for single subscription

        Returns:
              Response -- JSON serialized subscription
        """
        try:
            subscription = Subscription.objects.get(pk=pk)
            serializer = SubscriptionSerializer(subscription)
            return Response(serializer.data)
        except Subscription.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """Handle GET requests to get all subscriptions

        Returns:
            Response -- JSON serialized list of subscriptions
        """
        subscriptions = Subscription.objects.all()
        user = request.query_params.get('user')
        subscriptions = subscriptions.filter(follower_id = user)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized subscription instance
        """
        follower = RareUser.objects.get(pk=request.data["followerId"])
        author = RareUser.objects.get(pk=request.data["authorId"])
        subscription = Subscription.objects.create(
            follower_id = follower,
            author_id = author,
        )
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a subscription

        Returns:
            Response -- JSON serialized subscription instance
        """
        subscription = Subscription.objects.get(pk=pk)
        subscription.ended_on = request.data["ended_on"]
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        """Handles DELETE requests for a subscription

        Returns:
          Response - Empty body with 204 status code
        """
        subscription = Subscription.objects.get(pk=pk)
        subscription.delete()
        return Response({'message': 'Subscription deleted.'})
