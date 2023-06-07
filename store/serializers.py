from rest_framework import serializers
from .models import Product, Rating


class ProductListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ['name', 'category', 'image', 'price']

class  ProductDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = '__all__'

class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.product = validated_data.get('product', instance.user)
        instance.star = validated_data.get('star', instance.user)
        instance.save()
        return instance
    