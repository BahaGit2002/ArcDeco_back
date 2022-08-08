from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView
from .service import PaginatorShop
from .telepot import send_message
from .models import Product, Partner, Review, Window, Caregory, WindowModel, PedestalModel, Pedestal
from .serializers import (
    ShopSerializers, ContactSerializers, MessageSerializers, PartnerSerializers, ReviewSerializers, CategorySerializers,
    CalculatorWindowSerializer, CalculatorRackSerializer, ProductSerializers, ProductDetailSerializersall
                        )
from .filters import ProductFilter


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializers

    def get(self, request):
        category = Caregory.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)


class PartnerView(GenericAPIView):
    serializer_class = PartnerSerializers

    def get(self, request):
        partner = Partner.objects.all().order_by('place')
        serializer = PartnerSerializers(partner, many=True)
        return Response(serializer.data)


class ReviewView(GenericAPIView):
    serializer_class = ReviewSerializers
    queryset = Review.objects.order_by('place')

    def get(self, request):
        reviews = self.get_queryset()
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)


class ContactView(GenericAPIView):
    serializer_class = ContactSerializers

    def post(self, request):
        serializer = ContactSerializers(request.data)
        name = serializer.data['name']
        phone = serializer.data['phone_number']
        message = "*ЗАЯВКА С САЙТА*:" + "\n" + "*ИМЯ*: " + str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone)
        send_message(message)
        return Response({'answer': 'ok'}, status=status.HTTP_201_CREATED)


class MessageView(GenericAPIView):
    serializer_class = MessageSerializers

    def post(self, request):
        serializer = MessageSerializers(request.data)
        name = serializer.data['name']
        phone = serializer.data['phone_number']
        text = serializer.data['text']
        message = "*ЗАЯВКА С САЙТА* :" + "\n" + "*ИМЯ *: " + str(name) + "\n" + "*ТЕЛЕФОН* : " + str(phone) + '\n' + '*Писмо от клиента* :' + str(text)
        send_message(message)
        return Response({'answer': 'Ok'}, status=status.HTTP_201_CREATED)


class CalculatorWindowView(GenericAPIView):
    serializer_class = CalculatorWindowSerializer

    def post(self, request, **kwargs):
        serializer = CalculatorWindowSerializer(request.data)
        pk = kwargs['id']
        window_model = WindowModel.objects.filter(category_id=pk)
        length = serializer.data['length']
        width = serializer.data['width']
        count_window = serializer.data['count_window']
        window_dict = {}
        total = 0.0
        for window in window_model:
            if window.choice == 'dn' or window.choice == 'wh':
                if window.choice_window == 'true':
                    total += (length+0.5) * float(window.product.price)
                    window_dict[f'{window.product.category} {window.product.title}'] = length+0.5 * count_window
                else:
                    total += length * float(window.product.price)
                    window_dict[f'{window.product.category} {window.product.title}'] = length * count_window

            elif window.choice == 'bk':
                total += width * float(window.product.price) * 2
                window_dict[f'{window.product.category} {window.product.title}'] = width * 2 * count_window

            elif window.choice == 'dl':
                total += 2 * float(window.product.price)
                window_dict[f'{window.product.category} {window.product.title}'] = window.count * count_window

            else:
                if window.choice_window == 'true':
                    total += (length + 1) * float(window.product.price) * 2
                    window_dict[f'{window.product.category} {window.product.title}'] = (length+1) * 2 * count_window
                else:
                    total += length * float(window.product.price) * 2
                    window_dict[f'{window.product.category} {window.product.title}'] = f'{length * 2 * count_window}'
        window_dict['per window result'] = total
        window_dict['resalt'] = total * count_window
        return Response(window_dict)


class ProductViewall(ListAPIView):
    pagination_class = PaginatorShop
    serializer_class = ProductSerializers

    def get(self, request, **kwargs):
        filters = {}
        filters['window'] = Window.objects.filter(available=True, category_id=int(kwargs['category_id']))
        filter_1 = filters['window'].exists()
        filters['rack'] = Pedestal.objects.filter(category_id=int(kwargs['category_id']), available=True)
        filter_2 = filters['rack'].exists()
        filters['product'] = Product.objects.filter(category_id=int(kwargs['category_id']), available=True)
        if filter_1 is True:
            page = self.paginate_queryset(filters['window'])
            filters['window'] = page
        elif filter_2 is True:
            page = self.paginate_queryset(filters['rack'])
            filters['rack'] = page
        else:
            page = self.paginate_queryset(filters['product'])
            filters['product'] = page
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            filters, context=serializer_context)
        data = self.get_paginated_response(serializer.data)
        if (serializer.data['window'] == [] and
                serializer.data['rack'] == []
                and serializer.data['product'] == []):
            return Response({'answer': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return data


class ProductDetailViewall(ListAPIView):
    serializer_class = ProductDetailSerializersall

    def get(self, request, **kwargs):
        filters = {}
        filters['window_detail'] = Window.objects.filter(title=kwargs['name'], available=True)
        filters['rack_detail'] = Pedestal.objects.filter(title=kwargs['name'], available=True)
        filters['product_detail'] = Product.objects.filter(title=kwargs['name'], available=True)
        serializer = ProductDetailSerializersall(filters)
        if(serializer.data['window_detail'] == [] and
                serializer.data['rack_detail'] == []
                and serializer.data['product_detail'] == []):
            return Response({'answer': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data)


class ProductFilterView(ListAPIView):
    serializer_class = ProductSerializers
    pagination_class = PaginatorShop
    filter_backends = [DjangoFilterBackend]

    def filters(self, name, model, min_price, max_price, pk):
        filters = {}
        filters['model'] = model.objects.filter(category_id=pk, available=True)
        print(filters['model'])
        if filters['model'].exists() is True:
            if name is None:
                filters['model'] = filters['model'].filter(price__range=(min_price, max_price), category_id=pk, available=True)
            else:
                filters['model'] = filters['model'].filter(price__range=(min_price, max_price), title__icontains=name, category_id=pk, available=True)
        return filters['model']

    def get(self, request, **kwargs):
        max_price = self.request.query_params.get('max_price')
        min_price = self.request.query_params.get('min_price')
        name = self.request.query_params.get('name')
        pk = int(kwargs['category_id'])
        filters = {}
        if min_price is None:
            min_price = 0
        if max_price is None:
            max_price = 10**10
        if name is None:
            filters['product'] = self.filters(name, Product, min_price, max_price, pk)
            filters['window'] = Window.objects.filter(category_id=pk, available=True)
            filters['rack'] = Pedestal.objects.filter(category_id=pk, available=True)
        else:
            filters['product'] = self.filters(name, Product, min_price, max_price, pk)
            filters['window'] = Window.objects.filter(title__icontains=name, available=True, category_id=pk)
            filters['rack'] = Pedestal.objects.filter(title__icontains=name, available=True, category_id=pk)
        serializer = ProductSerializers(filters)
        return Response(serializer.data)
    filterset_class = ProductFilter



