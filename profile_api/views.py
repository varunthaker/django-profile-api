from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers


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