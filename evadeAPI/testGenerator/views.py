from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add_test_view():
    content = ""
    return Response(content, status=status.HTTP_200_OK)