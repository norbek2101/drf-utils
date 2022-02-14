from apps.models import Util
from rest_framework import serializers


class UtilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Util
        fields = '__all__'

