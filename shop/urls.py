from .views import (
    ContactView, MessageView, PartnerView, ReviewView,
    CategoryView, ProductFilterView, CalculatorWindowView, ProductViewall, ProductDetailViewall
                )
from django.urls import path


urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('message/', MessageView.as_view(), name='message'),
    path('partner/', PartnerView.as_view(), name='partner'),
    path('review/', ReviewView.as_view(), name='review'),
    path('calculator_window/<int:id>/', CalculatorWindowView.as_view()),
    # path('calculator_rack/<int:id>/', CalculatorRackView.as_view()),
    path('filter/<int:category_id>/', ProductFilterView.as_view()),
    path('product_list/<int:category_id>/', ProductViewall.as_view()),
    path('product_detail<str:name>/', ProductDetailViewall.as_view())
]
