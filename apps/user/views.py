from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from django.shortcuts import get_object_or_404
from rest_framework import status,viewsets
from rest_framework.response import Response

from apps.user.serializers import CreateUserSerializer, ListUserSerializer
from apps.user.models import UserAuth



## 
class CreateUser(CreateAPIView):
    """Api view for create an acount for one user"""

    serializer_class = CreateUserSerializer
    
    def create(self, request, *args, **kwargs):
        """
        Create one user.
        """
        # in the serializers, we lets go to validate passwor2, for it we lets go to pass the context at serializxers
        serializer = CreateUserSerializer(data=request.data, context=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        # we should delete password for security
        user_info = serializer.data
        user_info.pop("password")
        print(user_info)
        return Response(user_info, status=status.HTTP_201_CREATED)



class UserViewSet(viewsets.ViewSet):
    """
    Crud of users. 
    """
    queryset = UserAuth.objects.all()
    serializer_class = CreateUserSerializer
    # permission_classes = [IsAdminUser]
    
    def list(self, request):
        """
        List all users
        """
        queryset = UserAuth.objects.all()
        serializer = ListUserSerializer(queryset, many=True)
        return Response(serializer.data)

    # let's go to comment this create method because an user, in specifyc, that is not authenticated should see all data of all users 
    # def create(self, request, *args, **kwargs):
    #     """
    #     Create one user.
    #     """
        
    #     # in the serializers, we lets go to validate passwor2, for it we lets go to pass the context at serializxers
    #     serializer = CreateUserSerializer(data=request.data, context=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    