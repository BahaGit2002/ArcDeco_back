from django.db.models import Avg, FloatField
from rest_framework import serializers
from .models import Product, Partner, Review, Caregory, Window, WindowModel, PedestalModel, Pedestal


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Caregory
        fields = ('id', 'title')


class ShopSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'image',)


class ProductDetailSerializers(serializers.ModelSerializer):
    similar = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'image',
                  'poster1', 'poster2', 'poster3',
                  'category', 'poster', 'descriptions', 'similar')

    def get_similar(self, obj):
        product = Product.objects.exclude(title=obj.title).filter(category=obj.category)[:4]
        serializer = ShopSerializers(product, many=True)
        return serializer.data


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


class WindowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Window
        fields = ('id', 'title', 'image')


class WindowModelSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = WindowModel
        fields = ('product_name', 'measurement', 'count')


class WindowDetailSerializer(serializers.ModelSerializer):
    window = WindowModelSerializer(many=True)
    similar = serializers.SerializerMethodField()

    class Meta:
        model = Window
        fields = ('id', 'title', 'image', 'descriptions', 'window', 'similar')

    def get_similar(self, obj):
        window = Window.objects.exclude(title=obj.title)[:4]
        serializer = WindowSerializer(window, many=True)
        return serializer.data


class CalculatorWindowSerializer(serializers.Serializer):
    length = serializers.FloatField()
    width = serializers.FloatField()
    count_window = serializers.IntegerField(min_value=1)

    class Meta:
        fields = ('length', 'width', 'count_window')


class CalculatorRackSerializer(serializers.Serializer):
    width = serializers.FloatField()
    length = serializers.FloatField()
    count_rack_facial = serializers.IntegerField(min_value=0)
    count_rack_angular = serializers.IntegerField(min_value=0)

    class Meta:
        fields = ('width', 'length', 'count_rack_facial', 'count_rack_angular')


class RackSerializers(serializers.ModelSerializer):

    class Meta:
        model = Pedestal
        fields = ('id', 'title', 'image')


class ChoiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = PedestalModel
        fields = ('size_2', 'price_2')


class RackModelSerializer(serializers.ModelSerializer):
    size_2 = serializers.SerializerMethodField()

    class Meta:
        model = PedestalModel
        fields = ('id', 'title', 'poster', 'size_1', 'price_pm', 'price_sht', 'available', 'size_2')

    def get_size_2(self, obj):
        rack = PedestalModel.objects.filter(available=True, id=obj.id)
        serializer = ChoiceSerializers(rack, many=True)
        print(obj.id)
        return serializer.data


class RackDetailSerializer(serializers.ModelSerializer):
    rack = RackModelSerializer(many=True)
    similar = serializers.SerializerMethodField()

    class Meta:
        model = Pedestal
        fields = ('id', 'title', 'image', 'descriptions', 'rack', 'similar', )

    def get_similar(self, obj):
        rack = Pedestal.objects.exclude(title=obj.title)[:4]
        serializer = RackSerializers(rack, many=True)
        return serializer.data


class ProductSerializers(serializers.Serializer):
    rack = RackSerializers(many=True)
    window = WindowSerializer(many=True)
    product = ShopSerializers(many=True)


class ProductDetailSerializersall(serializers.Serializer):
    rack_detail = RackDetailSerializer(many=True)
    window_detail = WindowDetailSerializer(many=True)
    product_detail = ProductDetailSerializers(many=True)
