from django.shortcuts import render
from .serializers import RegisterSerializer
# Create your views here.
from rest_framework.generics import CreateAPIView


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

