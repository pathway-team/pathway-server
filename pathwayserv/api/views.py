from django.shortcuts import render
from pathwayserv.api.permissions import IsOwnerOrReadOnly, UserOrReadOnly
from rest_framework import permissions
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from pathwayserv.api.serializers import UserSerializer, RouteSerializer
from pathwayserv.api.models import Route, User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.generics import CreateAPIView

# Create your views here.

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return response({
        'users': reverse('users',request=request,format=format),
        'routes': reverse('routes',reques=request,format=format)
        })

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (
            permissions.AllowAny,
            UserOrReadOnly
            )
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RouteViewSet(viewsets.ModelViewSet):
    permission_classes = (
            permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly,
            )
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
