"""evadeAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from evader import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),
    
    # enable the admin interface
    url(r'^admin/', admin.site.urls),

    # User based routes
    url('user/add', views.registration_view, name="register"),
    url('user/login', obtain_auth_token, name="login"),
]
