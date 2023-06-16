from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from serializers import SubscriptionSerializer
from models import Subscription

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
        pass
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized subscription instance
        """
        pass
    
    def update(self, request, pk):
        """Handle PUT requests for a subscription

        Returns:
            Response -- JSON serialized subscription instance
        """
        pass
    
    def destroy(self, request, pk):
        """Handles DELETE requests for a subscription

        Returns:
          Response - Empty body with 204 status code
        """
        pass
