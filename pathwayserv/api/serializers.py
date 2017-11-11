#from django.contrib.auth.models import User, Group
from pathwayserv.api.models import Route, User, Run
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(
                validated_data['username'],
                )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = (
                'username',
                'url',
                'age',
                'weight',
                'height',
                'gender',
                'country',
                'active',
                'password'
                )

class RouteSerializer(serializers.HyperlinkedModelSerializer):
    center_lat = serializers.ReadOnlyField()
    center_long = serializers.ReadOnlyField()

    class Meta:
        model = Route
        fields = (
                'url',
                'id',
                'min_lat',
                'min_long',
                'max_lat',
                'max_long',
                'center_lat',
                'center_long',
                'user',
                'routeid',
                'parentid',
                'data',
                'atype'
                )
        # data = serializers.ListField(child=serializers.FloatField())

class RunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Run
        fields = (
                'url',
                'route_id',
                'user',
                'timestamp',
                'run_time'
                )
