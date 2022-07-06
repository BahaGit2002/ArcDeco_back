from django.contrib import admin
from .models import Product, Caregory, Partner


@admin.register(Caregory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created', 'uploded', 'available', 'price', 'amount']
    list_filter = ['available', 'created', 'uploded']
    list_editable = ['price', 'available']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['title', ]


