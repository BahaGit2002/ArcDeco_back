from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .service import PaginatorShop
from .telepot import send_message
from .models import Product, Partner, Review, Window, Caregory
from .serializers import ShopSerializers, ProductDetailSerializers, ContactSerializers, MessageSerializers, \
    FilterNameSerializers, PartnerSerializers, ReviewSerializers, CategorySerializers
from django.shortcuts import redirect, render


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializers

    def get(self, request):
        category = Caregory.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)


class ShopView(GenericAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ShopSerializers
    pagination_class = PaginatorShop

    def get_queryset(self):
        return Product.objects.filter(available=True)

    def get(self, request, **kwargs):
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
        product1 = Window.objects.all()
        for i in product1:
            print(i.product.price)
        serializer = ProductDetailSerializers(product)

        return Response(serializer.data)


class FilterNameView(GenericAPIView):
    serializer_class = FilterNameSerializers

    def get(self, request, **kwargs):
        title = kwargs['title']
        product = Product.objects.filter(available=True)
        product = product.filter(title__icontains=title)
        print(product)
        serializer = FilterNameSerializers(product, many=True)
        print(serializer.data)
        return Response(serializer.data)


class PartnerView(GenericAPIView):
    serializer_class = PartnerSerializers

    def get(self, request):
        partner = Partner.objects.all().order_by('place')
        serializer = PartnerSerializers(partner, many=True)
        print(serializer.data)
        return Response(serializer.data)


class ReviewView(GenericAPIView):
    serializer_class = ReviewSerializers

    def get(self, request):
        reviews = Review.objects.order_by('place')
        serializer = ReviewSerializers(reviews, many=True)
        return Response(serializer.data)


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

    def post(self, request):

        serializer = MessageSerializers(request.data)
        name = serializer.data['name']
        phone = serializer.data['phone_number']
        text = serializer.data['text']
        message = "*ЗАЯВКА С САЙТА*:" + "\n" + "*ИМЯ*: " + str(name) + "\n" + "*ТЕЛЕФОН* : " + str(phone) + '\n' + '*Писмо от клиента* :' + str(text)
        send_message(message)
        return Response('Ok')


# class RegisterView(GenericAPIView):
#     serializer_class = RegisterSerializers
#
#     def post(self, request):
#         serializer = RegisterSerializers(data=request.data)
#         data = {}
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.send()
#         if serializer.is_valid():
#             serializer.save()
#             data['response'] = True
#             return Response(data, status=status.HTTP_200_OK)
#         else:
#             data = serializer.errors
#             return Response(data)
def calculator(request):
    if request.method == 'POST':
        # vname_id = request.POST['']
        return redirect('addmovie')


