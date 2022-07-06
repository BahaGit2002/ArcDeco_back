from django.contrib import admin
from .models import ProductPortfolio


@admin.register(ProductPortfolio)
class ProductPortfolioAdmin(admin.ModelAdmin):
    list_display = ['title',  'created', 'uploded', 'pharetra']
    list_filter = ['created', 'uploded']
