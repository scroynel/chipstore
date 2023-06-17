from rest_framework import serializers
from .models import Product, Rating, Review


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    avg_star = serializers.IntegerField()
    class Meta: 
        model = Product
        fields = ['name', 'slug', 'category', 'image', 'price', 'avg_star']


class FilterReviewSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent = None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
    

class ReviewSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Review
        fields = ['user', 'text', 'children']


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class  ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    company = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = ReviewSerializer(many=True)
    class Meta: 
        model = Product
        fields = '__all__'

class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

    # создание и добавление без метода update и put во views
    # def create(self, validated_data):
    #     rating, _ = Rating.objects.update_or_create(
    #         user = validated_data.get('user', None),
    #         product = validated_data.get('product', None),
    #         defaults = {'star': validated_data.get('star', None)}
    #     )
    #     return rating

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.product = validated_data.get('product', instance.user)
        instance.star = validated_data.get('star', instance.user)
        instance.save()
        return instance
    

class RecursiveSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
    
    

class CreateReviewSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    class Meta:
        model = Review
        fields = ['user', 'text', 'children']