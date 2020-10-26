from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from evader.serializers import User_registration_serializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def registration_view(request):
    if request.method != 'POST':
        return Response('Only POSTs are allowed')
    try:
        print(request.data)
        response_data = {}
        serializer = User_registration_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data['message'] = 'succesfully created a new user.'
            response_data['email'] = user.email
            response_data['username'] = user.username
            token = Token.objects.get(user=user).key
            response_data['token'] =  token
            print("---------------->", token)
        else:
            print(serializer.errors)
            response_data = serializer.errors
    except:
        response_data = 'Failure while serializing data'

    return Response(response_data)