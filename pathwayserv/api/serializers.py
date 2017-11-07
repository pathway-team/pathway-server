#from django.contrib.auth.models import User, Group
from pathwayserv.api.models import Route, User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'user_name',
            'age',
            'weight',
            'height',
            'gender',
            'country',
            'active'
        )

'''
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
'''

class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = (
            'id',
            'bounding_box',
            'user',
            'routeid',
            'parentid',
            'data',
            'atype'
        )
        # data = serializers.ListField(child=serializers.FloatField())
