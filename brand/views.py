from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Brand
from .serializers import BrandModelSerializer


# Create your views here.


class BrandView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    # filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    lookup_field = "id"


class BrandView_1(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    # filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id", "name"]
    filterset_fields = ["id", "name"]
