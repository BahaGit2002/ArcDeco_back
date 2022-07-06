from rest_framework import serializers
from .models import ProductPortfolio


class PortfolioSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductPortfolio
        fields = ('id', 'title', 'poster',
                  'image1', 'image2', 'image3',
                  'pharetra', 'uorttitor', 'quisque', 'aliquet')


class PortfolioDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductPortfolio
        fields = ('id', 'title', 'pharetra',
                  'uorttitor', 'quisque', 'aliquet',
                  'poster', 'image1', 'image2', 'image3', 'discriptions')


