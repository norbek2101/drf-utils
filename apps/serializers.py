from .models import Util
from rest_framework import serializers


class UtilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Util
        fields = "__all__"

    # def to_representation(self, obj):
    #     return {
    #         "test": {"name":obj.name, "test2": obj.icon}
    #     }     

