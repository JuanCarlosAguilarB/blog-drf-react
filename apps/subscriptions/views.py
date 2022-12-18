# Django
from django.shortcuts import render

# Apps
from apps.subscriptions.serializers import SubscriptionsSerializers, TypesSubscriptionsSerializers, PlanSubscriptionsSerializers
from apps.subscriptions.models import Subscriptions, TypesOfSubscriptions, PlanSSubscriptions

# Django Rest
from rest_framework import viewsets
from rest_framework import generics

class SubscriptionsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Subscriptions.objects.all()
    # models = Subscriptions
    serializer_class = SubscriptionsSerializers
    # permission_classes = [IsAccountAdminOrReadOnly]
    
class TypesOfSubscriptionsView(generics.CreateAPIView):
    """
    Create the types of subscriptions: monthly, annual for example.
    """
    queryset = TypesOfSubscriptions.objects.all()
    serializer_class = TypesSubscriptionsSerializers
    # permission_classes = [IsAccountAdminOrReadOnly]
    
class PlanSSubscriptionsView(generics.ListCreateAPIView):
    """
    Create the plans of subscriptions: monthly, annual for example.
    """
    queryset = PlanSSubscriptions.objects.all()
    serializer_class = PlanSubscriptionsSerializers
    # permission_classes = [IsAccountAdminOrReadOnly]