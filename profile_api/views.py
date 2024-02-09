from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profile_api import serializers
from profile_api import models
from profile_api import permissions


class HelloApiView(APIView):
    """ TEST API VIEW"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        hello_object = ['Hello', 'python', 'Django', 'Hi']
        return Response({'message':'Hello Object', 'Obj': hello_object})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer._errors, 
                status=status.HTTP_400_BAD_REQUEST           
                )
    
    def put(self,request, pk=None):
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None): 
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        return Response({'method':"DELETE"})
    
class HelloViewSet(viewsets.ViewSet):

        def list(self, request):
            hello_viewset = ['Hello', 'python', 'Django', 'Hi']
            return Response({"viewset":hello_viewset})
        
class UserProfileViewSet(viewsets.ModelViewSet):
    """Creating and updating profiles"""
    serializer_class = serializers.UserProfileSerialiser
    queryset = models.UserProfile.objects.all()
    #User authentication
    authentication_classes = (TokenAuthentication,)
    #User access to a specific functionality 
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')