from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from .models import Brand
from .serializers import BrandModelSerializer, BrandNameSerializer, BrandByTypeSerializer
from rest_framework import viewsets


# Create your views here.


class BrandView(viewsets.ModelViewSet):
    """
    create:
    创建汽车品牌
    retrieve:
    获取汽车品牌详情
    update:
    修改汽车品牌信息
    destroy:
    删除汽车品牌
    list:
    获取所有的汽车品牌
    names:
    获取所有的汽车品牌名称
    partial_update:
    部分更新汽车品牌信息
    """
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    # filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id", "name"]
    filterset_fields = ["id", "name"]

    @action(methods=["get"], detail=False)
    def names(self, request):
        # 只获取id，和姓名接口
        # 名字和路由一定要一致，不然会报错
        queryset = self.queryset
        page = self.paginate_queryset(queryset)
        if page:
            serializer = BrandNameSerializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = BrandNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    # 通过ID获取该ID下面的所有TYPE数据
    def type(self, request, *args, **kwargs):

        type_set = self.get_object()
        serializer = BrandByTypeSerializer(instance=type_set)
        return Response(serializer.data)

# class BrandView_1(ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandModelSerializer
#     # filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
#
