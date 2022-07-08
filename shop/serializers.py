from rest_framework import serializers
from .models import Product, Partner, Review


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'price')


class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image',
                  'poster1', 'poster2', 'poster3',
                  'category', 'width', 'height', 'description')


class ContactSerializers(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)

    class Meta:
        fields = ('name', 'phone_number')


class MessageSerializers(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=1000)

    class Meta:
        fields = ('name', 'phone_number', 'text')


class FilterNameSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'image')


class PartnerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ('place', 'poster',)


class ReviewSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('place', 'name', 'text', 'video')





