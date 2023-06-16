from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rareapi.models.rare_user import RareUser
from rareapi.models.user import User
from rareapi.serializers.rare_user_serializer import RareUserSerializer, CreateRareUserSerializer

class RareUserView(ViewSet):
    """Rare API Rare Users"""
    def retrieve(self, request, pk):
        """GET Request for a single rare user"""
        try:
            rare_users = RareUser.objects.get(pk=pk)
            serializer = RareUserSerializer(rare_users)
            return Response(serializer.data)
        except RareUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of rare users"""
        rare_users = RareUser.objects.all()
        serializer = RareUserSerializer(rare_users, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """POST request to create a rare user"""
        user = User.objects.get(uid=request.META["HTTP_AUTHORIZATION"])
        serializer = CreateRareUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        