from django.shortcuts import render
from pathwayserv.api.permissions import IsOwnerOrReadOnly, UserOrReadOnly
from rest_framework import permissions
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from pathwayserv.api.serializers import UserSerializer, RouteSerializer, RunSerializer
from pathwayserv.api.models import Route, User, Run
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
    """
    retrieve:
    Return a JSON representation of the given user.

    list:
    Return a JSON list of all the users.

    create:
    Create a new user instance.
    """
    permission_classes = (
            permissions.AllowAny,
            UserOrReadOnly
            )
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RouteViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return a JSON representation of the given route.

    list:
    Return a JSON list of all the routes.

    create:
    Create a new route instance.
    """
    permission_classes = (
            permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly,
            )
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class RunViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return a JSON representation of the given run.

    list:
    Return a JSON list of all the runs.

    create:
    Create a new run instance.
    """
    permission_classes = (
            permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly,
            )
    queryset = Run.objects.all()
    serializer_class = RunSerializer
