from django.shortcuts import render
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class CartItemViews(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
