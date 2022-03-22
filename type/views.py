from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Type
from .serializers import TypeModelSerializer, TypeNameSerializer


# Create your views here.

class TypeView(viewsets.ModelViewSet):
    """
       create:
       创建车型
       retrieve:
       获取车型详情
       update:
       修改车型信息
       destroy:
       删除车型
       list:
       获取所有的车型
       names:
       获取所有的车型名称
       partial_update:
       部分更新车型
       """
    queryset = Type.objects.all()
    serializer_class = TypeModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id", "B_id"]
    filterset_fields = ["id"]
    lookup_field = "id"

    @action(methods=["get"], detail=False)
    def names(self, request):
        queryset = self.get_queryset()
        serializer = TypeNameSerializer(instance=queryset, many=Type)
        return Response(serializer.data)

    # @action(methods=["get"], detail=True)
    # def brands(self, request, *args, **kwargs):
    #     queryset = self.get_object()
    #     print(queryset)
    #     print(queryset.name)
    #     serializer = TypeByBrandSerializer(instance=queryset)
    #     return Response(serializer.data)
