from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .models import ProductPortfolio
from .serializers import PortfolioSerializers, PortfolioDetailSerializers


class PaginatorPortfolio(PageNumberPagination):
    page_size = 5
    max_page_size = 10000


class PortfolioView(GenericAPIView):
    queryset = ProductPortfolio.objects.all()
    # queryset = Product.objects.filter(available=True)
    serializer_class = PortfolioSerializers
    pagination_class = PaginatorPortfolio
    # print(pagination_class)

    def get_queryset(self):
        return ProductPortfolio.objects.all()

    def get(self, request):
        # product = Product.objects.filter(available=True)
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True)
        # page = self.paginate_queryset(queryset)
        # serializers = ShopSerializers(product, many=True)
        data = self.get_paginated_response(serializer.data)
        # pagination_class = PaginatorShop
        return data


class PortfolioDetailView(GenericAPIView):
    serializer_class = PortfolioDetailSerializers

    def get(self, request, **kwargs):
        pk = kwargs['id']
        product = ProductPortfolio.objects.get(id=pk)
        serializer = PortfolioDetailSerializers(product)
        return Response(serializer.data)

