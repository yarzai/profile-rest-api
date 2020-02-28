from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import HelloSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile


class HelloAPIView(APIView):
    """ Test APIView """

    serializer_class = HelloSerializer

    def get(self, reqest, formate=None):
        """ Return a list of APIView features """
        an_apiview = [
            'Users HTTP at function (get, post, put, patch, delete)',
            'Is similar to tradition Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello !', 'an_api': an_apiview})

    def post(self, reqest):
        """ Create hello meassage with our name """
        serializer = self.serializer_class(data=reqest.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle a partial update of an object """
        return Response({'message': 'PATCH'})

    def delete(self, reqest, pk=None):
        """ Delete an object """
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    serializer_class = HelloSerializer

    def list(self, reqest):
        """ Return a hello message """

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatially maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello !', 'a_viewset': a_viewset})

    def create(self, reqest):
        """ Create a new hello message """

        serializer = self.serializer_class(data=reqest.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, reqest, pk=None):
        """ Handle getting an objects """
        return Response({'HTTP_method': 'GET'})

    def update(self, reqest, pk=None):
        """ Handle updating an object """
        return Response({"HTTP_method": "PUT"})

    def partial_update(self, reqest, pk=None):
        """ Handle updating part of an object """
        return Response({"HTTP_method": "PATCH"})

    def destroy(self, reqest, pk=None):
        """ Handle removing an object """
        return Response({"HTTP_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating an updating profiles """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginAPIView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
