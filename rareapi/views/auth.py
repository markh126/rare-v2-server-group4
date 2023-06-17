from rest_framework.decorators import api_view
from rest_framework.response import Response
from rareapi.models import User


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if user is not None:
        data = {
            'id': user.id,
            'uid': user.uid,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
            'password': user.password,
            'is_staff': user.is_staff
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
    user = User.objects.create(
        bio=request.data['bio'],
        uid=request.data['uid'],
        first_name = request.data["firstName"],
        last_name = request.data["lastName"],
        email = request.data["email"],
        username = request.data["username"],
        password = request.data["password"],
        is_staff = request.data["isStaff"]
    )

    # Return the user info to the client
    data = {
        'id': user.id,
        'uid': user.uid,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'username': user.username,
        'password': user.password,
        'is_staff': user.is_staff
    }
    return Response(data)
