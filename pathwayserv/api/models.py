import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class User(AbstractUser):
    MALE   = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    # Table fields
    username = models.CharField(max_length=30, primary_key=True)
    phone_regex = RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
    phone_number = models.CharField(
            validators=[phone_regex],
            max_length=15,
            blank=True,
            help_text="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            ) # validators should be a list
    age = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0) # just store this as inches

    gender = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE,
        help_text="valid values are 'M' - male, 'F' - female"
    )

    country = models.CharField(max_length=255) # why is this needed?
    active = models.BooleanField(default=True)

class Route(models.Model):
    WALKING = 'W'
    RUNNING = 'R'
    BIKING  = 'B'

    ATYPE_CHOICES = {
        (WALKING, 'Walking'),
        (RUNNING, 'Running'),
        (BIKING,  'Biking')
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    min_lat  = models.FloatField()
    min_long = models.FloatField()
    max_lat  = models.FloatField()
    max_long = models.FloatField()

    @property
    def center_lat(self):
        return (self.min_lat + self.max_lat) / 2
        #return self.max_lat - (self.min_lat/2)

    @property
    def center_long(self):
        return (self.min_long + self.max_long) / 2
        #return self.max_long - (self.min_long/2)

    user = models.ForeignKey(
        User,
        help_text="The fully qualified URL of the user - http://<domain>/users/{username}/"
    )
    routeid = models.IntegerField()
    parentid = models.IntegerField()
    data = JSONField(
            help_text="GeoJSON route data"
            )
    atype = models.CharField(
            max_length=1,
            choices=ATYPE_CHOICES,
            default=WALKING,
            help_text="Valid values for this are 'W' - walking, 'R' - running, 'B' - biking"
            )

class Run(models.Model):
    route_id = models.ForeignKey(
            'Route',
            help_text="The fully qualified URL of the route - http://<domain>/routes/{routeid}/"
            )
    user = models.ForeignKey(
            'User',
            help_text="The fully qualified URL of the user - http://<domanin>/users/{username}/"
            )
    timestamp = models.DateField(auto_now_add=True)
    run_time = models.IntegerField() # measured in seconds

class Report(models.Model):
    data = JSONField()
