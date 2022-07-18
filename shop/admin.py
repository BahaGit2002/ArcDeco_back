from django.contrib import admin
from django.shortcuts import redirect, render
from .models import Product, Caregory, Partner, Review,  Window, WindowModel, PedestalModel, Pedestal
from django.urls import path


# @admin.register(Product)
class ChannelAdmin(admin.StackedInline):
    model = Product
    extra = 1


@admin.register(Caregory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title']
    inlines = [ChannelAdmin, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'created', 'available', 'price', 'amount']
    list_display_links = ['name', 'category', 'id']
    list_filter = ['available', 'created']
    list_editable = ['price', 'available']
    search_fields = ['name', ]
    change_list_template = "admin/model_change_list.html"
    # change_list_template = 'admin/'

    def get_urls(self):
        urls = super(ProductAdmin, self).get_urls()
        custom_urls = [
            path('import/', self.process_import_btmp, name='process_import'),
            # path('')
        ]
        return custom_urls + urls

    def process_import_btmp(self, request):
        if request.method == 'POST':
            product = Product.objects.all()
            percent = request.POST['text']
            for i in product:
                total = float(i.price) * (1 + int(percent) / 100)
                i.price = total
                i.save()
            return redirect('/admin/shop/product/')


# @admin.register(WindowModel)
class WindowModelAdmin(admin.StackedInline):
    model = WindowModel
    extra = 1


@admin.register(Window)
class WindowAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    # change_list_template = "admin/models_list.html"
    inlines = [WindowModelAdmin, ]


class PedestalModelAdmin(admin.StackedInline):
    model = PedestalModel
    extra = 1


@admin.register(Pedestal)
class PedestalAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    # change_list_template = "admin/models_list.html"
    inlines = [PedestalModelAdmin, ]
    # def get_urls(self):
    #     urls = super(WindowAdmin, self).get_urls()
    #     custom_urls = [
    #         path('calculator/', self.process_calculator_btmp, name='process_calculator'),
    #         # path('')
    #     ]
    #     return custom_urls + urls
    #
    # def process_calculator_btmp(self, request):
    #     print(request)
    #     if request.method == 'POST':
    #         product = Product.objects.all()
    #         print(product)
    #         # percent = request.POST['text']
    #         # for i in product:
    #         #     total = float(i.price) * (1 + 100)
    #         #     i.price = total
    #         #     i.save()
    #         return render(request, 'admin/calculator.html', {'product': product})


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    # pass
    list_display = ['place', 'title', ]
    list_display_links = ['place', 'title']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['place', 'name', 'grade', 'created']
    list_display_links = ['place', 'name']


admin.site.site_title = 'Админ-панель сайта о Art-Deco'
admin.site.site_header = 'Админ-панель сайта о Art-Deco'

# admin.site.register(WindowModel)
# @admin.register(WindowModel)
