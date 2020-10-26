"""evadeAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import include, url
from evader import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url('add', views.registration_view, name="register"),
    url('login', obtain_auth_token, name="login"),
]
