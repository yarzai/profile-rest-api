from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import status


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
