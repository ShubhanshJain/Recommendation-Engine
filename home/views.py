from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .product_recommendation import get_similar_product


# Create your views here.

class ProductAPI(APIView):
    def get(self, request):
        product = Product.objects.all().order_by('?')[:40]
        serializer = ProductSerializer(product, many = True)
        return Response({
            "all_product" : serializer.data
        })


class ProductDetailAPI(APIView):
    def get(self, request, id):
        product = Product.objects.get(id = id)
        serializer = ProductSerializer(product)
        similar_products = get_similar_product(id, 10)
        similar_products_serializer = ProductSerializer(similar_products, many=True)
        return Response({
            "product" : serializer.data,
            "similar_products" : similar_products_serializer.data
        })