from django.urls import path, include
from rest_framework import routers

from apps.user.views import CreateUser, UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('signup/', CreateUser.as_view())
]

urlpatterns += router.urls