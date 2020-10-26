"""evadeAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),
    
    # enable the admin interface
    url(r'^admin/', admin.site.urls),

    url('user/', include('evader.urls')),
    url('test', include('testGenerator.urls'))
]
