from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializer



class testApiView(APIView):

    serializer_class = serializer.TestSerializer

    def get(self, request , format=None):

        an_apiview =[
            # GET
            'api info content'
            # POST

            # PATCH

            # PUT

            # DELETE

        ]

        return Response({'message':'Testing','an_apiview':an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST )

    def put(self, request, pk=None):
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        return Response({'Method':'PATCH'})

    def delete(self, request, pk=None):
        return Response({'Method':'DELETE'})

class testViewSet(viewsets.ViewSet):

    serializer_class = serializer.TestSerializer

    def list(self, request):
        a_viewset =[
            'Uses action (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionally with less code',
        ]

        return Response({'message':'Testing', 'a_viewset':a_viewset})

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !'
            return  Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):

        return Response({'http_method':'PATCH'})

    def destory(self, request, pk=None):

        return Response({'http_method':'DELETE'})