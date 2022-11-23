from django.db import models

# Create your models here.


class Countries(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'countries'

class UserAuth(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    photo = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'user_auth'
