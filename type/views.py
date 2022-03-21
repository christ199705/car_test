from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Type
from .serializers import TypeModelSerializer


# Create your views here.

class TypeView_1(ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id","B_id"]
    filterset_fields = ["id"]


class TypeView_2(RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeModelSerializer
    lookup_field = "id"
