from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Rating
from .serializers import ProductListSerializer, ProductDetailSerializer, CreateRatingSerializer

class ProductView(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'slug'
    def get_queryset(self):
        products = Product.objects.all()
        return products

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        
class CreateRatingView(APIView):
    def post(self, request):
        serializer = CreateRatingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(status=201)
        else:
            return Response(status=400)
    
    def put(self, request, *args, **kwargs):
        rating = Rating.objects.get(user = request.user)
        serializer = CreateRatingSerializer(data = request.data, instance=rating)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(status=400)

