from django.shortcuts import render
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from pathwayserv.api.serializers import UserSerializer, RouteSerializer
from pathwayserv.api.models import Route, User

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    '''
    API Endpoint that allows users to be viewed or edited.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
'''

class RouteViewSet(viewsets.ModelViewSet):
    '''
    API Endpoint that allows routes to be viewed, edited, or created
    '''
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
