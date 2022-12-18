# django rest framework
from rest_framework import serializers

# Apps
from apps.subscriptions.models import Subscriptions, TypesOfSubscriptions, PlanSSubscriptions

class SubscriptionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subscriptions
        fields = "__all__"
        
class TypesSubscriptionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = TypesOfSubscriptions
        fields = "__all__"
        

class PlanSubscriptionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = PlanSSubscriptions
        fields = "__all__"
        