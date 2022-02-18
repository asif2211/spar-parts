from django.shortcuts import render
from .serializers import ProductSerializer, ItemSerializer, SaleSerializer
from rest_framework import viewsets
from .models import Product, Item, Sale


class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SaleView(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
