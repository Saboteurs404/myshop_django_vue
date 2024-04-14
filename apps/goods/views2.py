from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from apps.goods.models import *
import json

from apps.goods.serializers import GoodsSerizlizer
from rest_framework.views import APIView
from rest_framework.response import Response
class GoodsList(APIView):
    def get(self, request):
        goods = Goods.objects.all()[:10]
        goods_json = GoodsSerizlizer(goods, many=True)
        return Response(goods_json.data)


from rest_framework import mixins
from rest_framework import generics
class GoodsListView_mixins(mixins.ListModelMixin,generics.GenericAPIView):
    '''
    list:
        返回所有数据
    retrieve:
        返回单条数据实例
    create:
        新增数据
    update:
        修改数据
    partial_update:
        修改部分数据
    delete:
        删除数据
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerizlizer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class GoodsListView_List(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerizlizer