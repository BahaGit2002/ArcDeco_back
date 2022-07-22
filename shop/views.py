from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView
from .service import PaginatorShop
from .telepot import send_message
from .models import Product, Partner, Review, Window, Caregory, WindowModel
from .serializers import (
    ShopSerializers, ProductDetailSerializers, ContactSerializers, MessageSerializers,
    PartnerSerializers, ReviewSerializers, CategorySerializers, WindowSerializer,
    CalculatorWindowSerializer
                        )
from .filters import ProductFilter


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializers

    def get(self, request):
        category = Caregory.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)


class ProductView(GenericAPIView):
    serializer_class = ShopSerializers
    pagination_class = PaginatorShop
    queryset = Product.objects.filter(available=True)

    def get(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True)
        data = self.get_paginated_response(serializer.data)
        return data


class ProductDetailView(GenericAPIView):
    serializer_class = ProductDetailSerializers

    def get(self, request, **kwargs):
        pk = kwargs['id']
        product = Product.objects.get(id=pk)
        serializer = ProductDetailSerializers(product)

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
        return Response('Ok')


class WindowView(GenericAPIView):
    serializer_class = WindowSerializer
    pagination_class = PaginatorShop

    # def get(self, request):
    #     window = Window.objects.all()
    #     serializer = WindowSerializer(window, many=True)
    #     # if serializer.is_valid():
    #     #     pass
    #     return Response(serializer.data)

    def get_queryset(self):
        return Window.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True)
        data = self.get_paginated_response(serializer.data)
        return data


class ProductFilterView(ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ShopSerializers
    filter_backends = [DjangoFilterBackend]
    pagination_class = PaginatorShop
    filterset_class = ProductFilter


class CalculatorWindowView(GenericAPIView):
    serializer_class = CalculatorWindowSerializer

    def post(self, request, **kwargs):
        serializer = CalculatorWindowSerializer(request.data)
        pk = kwargs['id']
        window = Window.objects.get(id=pk)
        window_model = WindowModel.objects.filter(category=window)
        length = serializer.data['length']
        width = serializer.data['width']
        count_window = serializer.data['count_window']
        total = 0.0
        for window in window_model:
            if window.choice == 'dn' or window.choice == 'wh':
                if window.choice_window == 'true':
                    total += (length+0.5) * float(window.price)
                else:
                    total += length * float(window.price)

            elif window.choice == 'bk':
                total += width * float(window.price) * 2

            elif window.choice == 'dl':
                total += window.count * float(window.price)

            else:
                if window.choice_window == 'true':
                    total += (length + 1) * float(window.price) * 2
                else:
                    total += length * float(window.price) * 2

        resalt = total * count_window
        return Response({'resalt': resalt, 'per window result': total})


