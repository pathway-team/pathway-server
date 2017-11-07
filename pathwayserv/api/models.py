import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class User(models.Model):
    '''

    '''
    MALE   = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    # Table fields
    user_name   = models.CharField(max_length=30,primary_key=True)
    first_name  = models.CharField(max_length=30)
    last_name   = models.CharField(max_length=30)
    age         = models.IntegerField()
    weight      = models.IntegerField()
    height      = models.IntegerField() # just store this as inches

    gender = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE
    )

    country     = models.CharField(max_length=255) # why is this needed?
    active      = models.BooleanField()
    '''
    password_id = models.ForeignKey(
        'Pword',
        default="",
        # if a user is removed, remove their password as well?
        # we can also have an account deactivated option.
        on_delete=models.CASCADE
    )
    '''

class Pword(models.Model):
    '''

    '''
    # update this later, this needs to be a hash of the password (sha256) and a
    # salt. Need to determine the salt function to use.
    p_hash = models.CharField(max_length=256)

class Route(models.Model):
    '''

    '''
    WALKING = 'W'
    RUNNING = 'R'
    BIKING  = 'B'

    ATYPE_CHOICES = {
        (WALKING, 'Walking'),
        (RUNNING, 'Running'),
        (BIKING,  'Biking')
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bounding_box = JSONField()
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
    '''

    '''
    '''
    user_name = models.ForeignKey(
       'User'
    )
    '''
    route_id = models.ForeignKey(
       'Route'
    )
    timestamp = models.DateField(auto_now_add=True)
    run_time  = models.IntegerField() # measured in seconds

class Report(models.Model):
    '''

    '''
    data = JSONField()
