from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from evader.serializers import User_registration_serializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def registration_view(request):
    if request.method != 'POST':
        content = "Only POSTs are allowed"
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    try:
        content = {}
        serializer = User_registration_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            content['message'] = 'succesfully created a new user.'
            content['email'] = user.email
            content['username'] = user.username
            token = Token.objects.get(user=user).key
            content['token'] =  token
            print("---------------->", token)
        else:
            print(serializer.errors)
            content = serializer.errors
    except:
        content = 'Failure while serializing data'

    return Response(content, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def dashboard_view(request):
    content = ""
    return Response(content, status=status.HTTP_200_OK)
