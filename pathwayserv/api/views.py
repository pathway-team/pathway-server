from django.shortcuts import render
from pathwayserv.api.permissions import IsOwnerOrReadOnly, UserOrReadOnly
from rest_framework import permissions
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from pathwayserv.api.serializers import UserSerializer, RouteSerializer, RunSerializer
from pathwayserv.api.models import Route, User, Run
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, list_route
from rest_framework.reverse import reverse
from rest_framework.generics import CreateAPIView, ListAPIView

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
#class RouteViewSet(generics.ListAPIView):
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
    serializer_class = RouteSerializer

    queryset = Route.objects.all()

    '''
    @list_route()
    def near_by(self, request):
        min_lat = self.request.query_params.get('min_lat',None)
        min_lon = self.request.query_params.get('min_long',None)
        max_lat = self.request.query_params.get('max_lat',None)
        max_lon = self.request.query_params.get('max_long',None)
        n_bbox = [min_lat,min_lon,max_lat,max_lon]

    '''

    def get_queryset(self):
        queryset = Route.objects.all()

        min_lat = self.request.query_params.get('min_lat',None)
        min_lon = self.request.query_params.get('min_long',None)
        max_lat = self.request.query_params.get('max_lat',None)
        max_lon = self.request.query_params.get('max_long',None)
        n_bbox = [min_lat,min_lon,max_lat,max_lon]

        if None not in n_bbox:
            #queryset = Route.objects.filter(bounding_box__gte=center)
            queryset = Route.objects.filter(center_long__gte=min_lon)
                                    .filter(center_long__lte=max_lon)
                                    .filter(center_lat__gte=min_lat)
                                    .filter(center_lat__lte=max_lat)
            n_bbox = map(float, n_bbox)
            print("hey")
        return queryset


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
