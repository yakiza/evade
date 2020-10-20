from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from evader.serializers import user_registration_serializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def registration_view(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        responseData = {}
        serializer = user_registration_serializer(data=request.data)  
        if serializer.is_valid():
            user = serializer.save()
            responseData['message'] = "succesfully created a new user."
            responseData['email'] = user.email
            responseData['username'] = user.username
            token = Token.objects.get(user=user).key
            responseData['token'] =  token
            print("---------------->", token)
        else:
            responseData = serializer.errors
    except :
        responseData = "Failure while serializing data"

    return Response(responseData)