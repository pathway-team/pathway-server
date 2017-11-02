from django.db import models
from django.contrib.postgres.fields import JSONField

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
    active      =
    password_id = models.ForeignKey(
        'Passsword',
        # if a user is removed, remove their password as well?
        # we can also have an account deactivated option.
        on_delete=models.CASCADE
    )

class Password(models.Model):
    '''

    '''
    # update this later, this needs to be a hash of the password (sha256) and a
    # salt. Need to determine the salt function to use.
    p_hash = models.CharField(max_length=256)

class Route(models.Model):
    '''

    '''
    # for now this can just be a uuid
    id = models.UUIDField(primar_key=True, default=uuid.uuid4, editable=False)
    # what level of precision do we want on each coord?
    # Will need to define a Geo coordinate type
    min_point = JSONField()
    max_point = JSONField()
    center    = JSONField()

class Run(models.Model):
    '''

    '''
    user_name = models.ForeignKey(
       'User'
    )
    route_id = models.ForeignKey(
       'Route'
    )
    timestamp = models.DateField(auto_now_add=True)
    run_time  = models.IntegerField() # measured in seconds

class Report(models.Model):
    '''

    '''
    data = JSONField()
