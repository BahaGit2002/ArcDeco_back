from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404, RetrieveAPIView

from .models import ProductPortfolio
from .serializers import PortfolioSerializers, PortfolioDetailSerializers


class PaginatorPortfolio(PageNumberPagination):
    page_size = 5
    max_page_size = 10000


class PortfolioView(GenericAPIView):
    queryset = ProductPortfolio.objects.all()
    serializer_class = PortfolioSerializers
    pagination_class = PaginatorPortfolio

    def get_queryset(self):
        return ProductPortfolio.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True)
        data = self.get_paginated_response(serializer.data)
        return data


class PortfolioDetailView(RetrieveAPIView):
    queryset = ProductPortfolio.objects.all()
    serializer_class = PortfolioDetailSerializers


