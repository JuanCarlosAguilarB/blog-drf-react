# Django
from django.urls import path, include

# Django rest
from rest_framework import routers

# Apps
from apps.subscriptions.views import SubscriptionsViewSet, TypesOfSubscriptionsView, PlanSSubscriptionsView


router = routers.SimpleRouter()
router.register(r'subscriptions', SubscriptionsViewSet)

urlpatterns = [
    path('types', TypesOfSubscriptionsView.as_view()),
    path('plans', PlanSSubscriptionsView.as_view()),
]

urlpatterns += router.urls