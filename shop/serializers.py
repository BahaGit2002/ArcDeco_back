from django.db.models import Avg, FloatField
from rest_framework import serializers
from .models import Product, Partner, Review, Star


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
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('place', 'name', 'text', 'video', 'middle_star')

    def get_middle_star(self, obj):
        return Star.objects.aggregate(Avg('grade', output_field=FloatField()))['grade__avg']


# class ReviewSerializer(serializers.ListSerializer):
#     middle_star = serializers.FloatField(read_only=True)
#     reviews = ReviewSerializers(many=True, read_only=True)
#     # print(reviews.data)
#
#     class Meta:
#         fields = ['middle_star', 'reviews']




