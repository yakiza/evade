from django.contrib.auth.models import User, Group
from evader.serializers import user_registration_serializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = user_registration_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "successfully registered a new user! Hooray!"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)
