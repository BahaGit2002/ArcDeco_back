from django.contrib import admin
from django.shortcuts import redirect
from .models import Product, Caregory, Partner, Review,  Window, WindowModel, PedestalModel, Pedestal
from django.urls import path


class ChannelAdmin(admin.StackedInline):
    model = Product
    extra = 1


@admin.register(Caregory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created', 'available', 'price', ]
    list_display_links = ['title', 'category', 'id']
    list_filter = ['available', 'created']
    list_editable = ['price', 'available']
    search_fields = ['title', ]
    save_on_top = True
    change_list_template = "admin/model_change_list.html"

    def get_urls(self):
        urls = super(ProductAdmin, self).get_urls()
        custom_urls = [
            path('import/', self.process_import_btmp, name='process_import'),
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


class WindowModelAdmin(admin.StackedInline):
    model = WindowModel
    fields = ('product', 'choice', 'measurement', 'count', 'choice_window')
    autocomplete_fields = ('product', )
    extra = 1


@admin.register(Window)
class WindowAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    save_on_top = True
    inlines = [WindowModelAdmin, ]


class PedestalModelAdmin(admin.StackedInline):
    model = PedestalModel
    fields = ('poster', 'title', 'choice', 'measurement',
              ('size_1', 'price_pm', 'price_sht'), ('available', 'size_2', 'price_2'), 'choice_1')
    extra = 1


@admin.register(Pedestal)
class PedestalAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title', ]
    inlines = [PedestalModelAdmin, ]
    save_on_top = True


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['place', 'title', ]
    list_display_links = ['place', 'title']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['place', 'name', 'grade', 'created']
    list_display_links = ['place', 'name']


admin.site.site_title = 'Админ-панель сайта о Art-Deco'
admin.site.site_header = 'Админ-панель сайта о Art-Deco'



