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
    age = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0) # just store this as inches

    gender = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE
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
        default=""
    )
    routeid = models.IntegerField()
    parentid = models.IntegerField()
    data = JSONField()
    atype = models.CharField(
        max_length=1,
        choices=ATYPE_CHOICES,
        default=WALKING
    )

class Run(models.Model):
    route_id = models.ForeignKey(
            'Route'
            )
    user = models.ForeignKey(
            'User'
            )
    timestamp = models.DateField(auto_now_add=True)
    run_time = models.IntegerField() # measured in seconds

class Report(models.Model):
    data = JSONField()
