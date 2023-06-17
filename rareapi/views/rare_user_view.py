from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rareapi.models.rare_user import RareUser
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
        user = RareUser.objects.get(uid=request.META["HTTP_AUTHORIZATION"])
        serializer = CreateRareUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(uid=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update a rare user"""
        rare_user = RareUser.objects.get(pk=pk)
        user = RareUser.objects.get(uid=request.META["HTTP_AUTHORIZATION"])
        rare_user.first_name = request.data['first_name']
        rare_user.last_name = request.data['last_name']
        rare_user.bio = request.data['bio']
        rare_user.profile_image_url = request.data['profile_image_url']
        rare_user.email = request.data['email']
        rare_user.active = request.data['active']
        rare_user.is_staff = request.data['is_staff']
        rare_user.uid = user
        rare_user.save()
        return Response({'message': 'Rare User Updated'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to destroy a rare user"""
        rare_user = RareUser.objects.get(pk=pk)
        rare_user.delete()
        return Response({'message': 'Rare User Destroyed'}, status=status.HTTP_204_NO_CONTENT)
