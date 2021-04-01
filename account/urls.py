from django.urls import include, path
from rest_framework import routers
from .views import *


routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'group', GroupViewSet)
urlpatterns = routers.urls



