import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Util
from .serializers import UtilSerializer


class UtilView(APIView):

    def get(self, request):
        utils = Util.objects.all()
        serializer = UtilSerializer(utils, many=True)
        return Response(
            {
                "results": serializer.data,
                "count": utils.count()
            }
        )

    def post(self, request):
        serializer = UtilSerializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save()

            return Response(
                    {
                        "response": 'The data has been successfully created',
                    },
                    status=status.HTTP_201_CREATED
                )
        else:
            return Response(
                {
                    "error": serializer.errors
                },
                status=status.HTTP_404_NOT_FOUND
            )        

    def put(self, request):
        try:
            util = request.data['id'][0]
        except Exception as e:
            return Response(
                {
                    "error": "field error: 'id' is not found",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            util = Util.objects.get(id=util)
        except:
            return Response(
                {
                    "error": "The requested 'id' is not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UtilSerializer(instance=util, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                    {
                        "response": 'The data has been successfully updated'
                    },
                     status=status.HTTP_206_PARTIAL_CONTENT
                )            
        else:
            return Response(
                {
                    "error": serializer.errors
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request):
        pass