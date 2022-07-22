from django.db.models import Avg, FloatField
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Partner, Review, Caregory, Window, WindowModel
from django.conf import settings
from django.core.mail import send_mail


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Caregory
        fields = ('id', 'title')


class ShopSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'price')


class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image',
                  'poster1', 'poster2', 'poster3',
                  'category', 'poster', 'descriptions')


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

#
# class FilterNameSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'image')


class PartnerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ('place', 'poster',)


class ReviewSerializers(serializers.ModelSerializer):
    middle_star = serializers.SerializerMethodField()
    count_review = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('place', 'name', 'text', 'video', 'middle_star', 'count_review')

    def get_middle_star(self, obj):
        return Review.objects.aggregate(Avg('grade', output_field=FloatField()))['grade__avg']

    def get_count_review(self, obj):
        return len(Review.objects.all())


class ProductFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class WindowModelSerializer(serializers.ModelSerializer):
    # product_name = serializers.RelatedField(source='category', read_only=True)
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = WindowModel
        fields = ('product_name', 'measurement', 'count', 'price')


class WindowSerializer(serializers.ModelSerializer):
    window = WindowModelSerializer(many=True)

    class Meta:
        model = Window
        fields = ('id', 'title', 'image', 'window', )


class CalculatorWindowSerializer(serializers.Serializer):
    length = serializers.FloatField()
    width = serializers.FloatField()
    count_window = serializers.IntegerField(min_value=1)

    class Meta:
        fields = ('length', 'width', 'count_window')
