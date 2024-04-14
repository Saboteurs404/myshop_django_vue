from rest_framework import serializers
from .models import *

class GoodsSerizlizer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)


class GoodsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Goods
        fields = "__all__"