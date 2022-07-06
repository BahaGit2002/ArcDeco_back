from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView
from .service import PaginatorShop
from .telepot import send_message
from rest_framework import filters
from .models import Product
from .serializers import ShopSerializers, ProductDetailSerializers, ContactSerializers, MessageSerializers, FilterNameSerializers, PartnerSerializers


class ShopView(GenericAPIView):
    queryset = Product.objects.filter(available=True)
    # queryset = Product.objects.filter(available=True)
    serializer_class = ShopSerializers
    pagination_class = PaginatorShop
    # print(pagination_class)

    def get_queryset(self):
        return Product.objects.filter(available=True)

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


class ProductDetailView(GenericAPIView):
    serializer_class = ProductDetailSerializers

    def get(self, request, **kwargs):
        pk = kwargs['id']
        product = Product.objects.get(id=pk)
        serializer = ProductDetailSerializers(product)

        return Response(serializer.data)


class FilterNameView(GenericAPIView):
    serializer_class = FilterNameSerializers

    def get(self, request, **kwargs):
        title = kwargs['title']
        # print(kwargs)
        product = Product.objects.filter(available=True)
        product = product.filter(title__icontains=title)
        print(product)
        serializer = FilterNameSerializers(product, many=True)
        print(serializer.data)
        return Response(serializer.data)


# class PartnerView(GenericAPIView):
#     serializer_class = PartnerSerializers
#
#     def get(self, request):



class ContactView(GenericAPIView):
    serializer_class = ContactSerializers

    def post(self, request):

        serializer = ContactSerializers(request.data)
        name = serializer.data['name']
        phone = serializer.data['phone_number']
        message = "*ЗАЯВКА С САЙТА*:" + "\n" + "*ИМЯ*: " + str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone)
        send_message(message)
        return Response('Ok')


class MessageView(GenericAPIView):
    serializer_class = MessageSerializers
    # pagination_class = PaginatorShop

    def post(self, request):

        serializer = MessageSerializers(request.data)
        name = serializer.data['name']
        phone = serializer.data['phone_number']
        text = serializer.data['text']
        message = "*ЗАЯВКА С САЙТА*:" + "\n" + "*ИМЯ*: " + str(name) + "\n" + "*ТЕЛЕФОН* : " + str(phone) + '\n' + '*Писмо от клиента* :' + str(text)
        send_message(message)
        return Response('Ok')






