from django_filters.rest_framework import RangeFilter, FilterSet, BaseInFilter, CharFilter
from .models import Product


class CharFilterInFilter(BaseInFilter, CharFilter):
    pass


class ProductFilter(FilterSet):
    category = CharFilterInFilter(field_name='category__title', lookup_expr='in')
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    price = RangeFilter()

    class Meta:
        model = Product
        fields = ['price', 'category', 'name']
