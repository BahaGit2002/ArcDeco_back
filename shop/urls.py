from .views import ProductView, ProductDetailView, ContactView, MessageView, PartnerView, ReviewView, \
    CategoryView, ProductFilterView, WindowView, CalculatorWindowView
from django.urls import path


urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('product/', ProductView.as_view(), name='product'),
    path('product_detail/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('message/', MessageView.as_view(), name='message'),
    path('filter/', ProductFilterView.as_view(), name='filter'),
    path('partner/', PartnerView.as_view(), name='partner'),
    path('review/', ReviewView.as_view(), name='review'),
    path('calculator/<int:id>/', CalculatorWindowView.as_view()),
    path('filter/', ProductFilterView.as_view(), name='filter'),
    path('window/', WindowView.as_view(), name='window'),
]
#
