from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.models import Util
from apps.serializers import UtilSerializer


class UtilView(APIView):

    def get(self, request):
        utils = Util.objects.all()
        serializer = UtilSerializer(utils, many=True)
        return Response(
            {'results': serializer.data}
        )

    def post(self, request):
        serializer = UtilSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"response": serializer.data}
            )
