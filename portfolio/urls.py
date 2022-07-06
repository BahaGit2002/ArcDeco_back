from .views import PortfolioView, PortfolioDetailView
from django.urls import path

urlpatterns = [
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('detail/<int:id>/', PortfolioDetailView.as_view(), name='detail'),
]