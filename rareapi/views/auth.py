from rest_framework.decorators import api_view
from rest_framework.response import Response
from rareapi.models.rare_user import RareUser


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    rare_user = RareUser.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if rare_user is not None:
        data = {
            'id': rare_user.id,
            'uid': rare_user.uid,
            'first_name': rare_user.first_name,
            'last_name': rare_user.last_name,
            'bio': rare_user.bio,
            'profile_image_url': rare_user.profile_image_url,
            'email': rare_user.email,
            'active': rare_user.active,
            'is_staff': rare_user.is_staff
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the rareapi_user table
    rare_user = RareUser.objects.create(
        uid=request.data['uid'],
        first_name = request.data["firstName"],
        last_name = request.data["lastName"],
        bio = request.data["bio"],
        profile_image_url = request.data["profileImageUrl"],
        email = request.data["email"],
    )

    # Return the user info to the client
    data = {
            'id': rare_user.id,
            'uid': rare_user.uid,
            'first_name': rare_user.first_name,
            'last_name': rare_user.last_name,
            'bio': rare_user.bio,
            'profile_image_url': rare_user.profile_image_url,
            'email': rare_user.email,
            'active': rare_user.active,
            'is_staff': rare_user.is_staff
    }
    return Response(data)
