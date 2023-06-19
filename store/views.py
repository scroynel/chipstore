from django.shortcuts import render
from django.db import models
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product, Rating
from .serializers import ProductListSerializer, ProductDetailSerializer, CreateRatingSerializer, CreateReviewSerializer

# class ProductView(viewsets.ReadOnlyModelViewSet):
#     lookup_field = 'slug'
#     def get_queryset(self):
#         products = Product.objects.all().annotate(
#             avg_star = models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
#         )
#         return products

#     def get_serializer_class(self):
#         if self.action == 'list':
#             return ProductListSerializer
#         elif self.action == 'retrieve':
#             return ProductDetailSerializer
        

class ProductListView(APIView):
    def get(self, request):
        queryset = Product.objects.all().annotate(
            avg_star = models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data)
    

class ProductDetailView(APIView):
    def get(self, request, pk):
        queryset = Product.objects.get(pk = pk)
        serializer = ProductDetailSerializer(queryset)
        return Response(serializer.data)

        
class CreateRatingView(APIView):
    permission_classes = [IsAuthenticated, ]
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
        

class ReviewView(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        serializer = CreateReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

