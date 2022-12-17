# Django 
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()
class Subscriptions(models.Model):
    """Model for subscriptions"""
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    
class TypesOfSubscriptions(models.Model):
    """Model for to represent the types of the subscriptions"""
    
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "types_subscriptions"
  
class PlanSSubscriptions(models.Model):
    """Model for to represent the plans of subscriptions."""
    
    subscription = models.ForeignKey(User, verbose_name="subscription", on_delete=models.PROTECT)
    type = models.ForeignKey(TypesOfSubscriptions,  on_delete=models.PROTECT)
    price = models.FloatField()
    
    class Meta:
        db_table = "plans_subscriptions"

class SubscriptionsForUsers(models.Model):
    """Model for to represent the subscription of an user"""
    
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.PROTECT)
    plan = models.ForeignKey(PlanSSubscriptions,  on_delete=models.PROTECT)
   
    # en caso de haber un descuento especial, por temporada o demás.
    discount_applied = models.FloatField(default=0.0, blank=True, null=True)
    
    class Meta:
        db_table = "subscriptions_for_users"
    