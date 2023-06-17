from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rareapi.models.user import User
from rareapi.serializers.user_serializer import UserSerializer

class UserView(ViewSet):
    """Rare API Users"""
    def retrieve(self, request, pk):
        """GET Request for a single user"""
        try:
            users = User.objects.get(pk=pk)
            serializer = UserSerializer(users)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET Request for a list of users"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)
