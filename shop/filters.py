from django_filters.rest_framework import RangeFilter, FilterSet, BaseInFilter, CharFilter, NumberFilter
from .models import Product, Pedestal, Window


class ProductFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['name', 'min_price', 'max_price', ]
