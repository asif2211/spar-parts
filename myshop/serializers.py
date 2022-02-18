from rest_framework import serializers
from .models import Product, Item, Sale


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        # fields = ('id','title','description','fileextion')
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    # gist_set = TodoSerializer()
    class Meta:
        model = Product
        # fields = ('id', 'gist_set', 'comments',)
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    # gist_set = TodoSerializer()
    class Meta:
        model = Sale
        # fields = ('id', 'gist_set', 'comments',)
        fields = "__all__"
