from django.urls import path, include
from rest_framework import routers

from apps.user.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls