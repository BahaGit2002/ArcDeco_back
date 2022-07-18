from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


class Caregory(models.Model):
    title = models.CharField('название', max_length=100, db_index=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField('наименование', max_length=100)
    descriptions = models.TextField(max_length=1000, default='')
    image = models.ImageField('фото продукта', upload_to='products', blank=True)
    poster = models.ImageField('размер', upload_to='products/poster', blank=True)
    category = models.ForeignKey(Caregory, verbose_name='категория', on_delete=models.CASCADE)
    price = models.DecimalField('цена', max_digits=100, decimal_places=2)
    available = models.BooleanField('наличие', default=True)
    poster1 = models.ImageField(upload_to='products/poster1', blank=True)
    poster2 = models.ImageField(upload_to='products/poster2', blank=True)
    poster3 = models.ImageField(upload_to='products/poster3', blank=True)
    created = models.DateTimeField('дата создание', auto_now_add=True)
    uploded = models.DateTimeField('дата обновление', auto_now=True)
    amount = models.IntegerField('количество', default=0)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Window(models.Model):
    true = 'tr'
    false = 'fa'
    choice_status_2 = [
        (true, 'Да'),
        (false, 'Нет')
    ]
    title = models.CharField('Названия', max_length=100, default='')
    image = models.ImageField('Фото', upload_to='window', blank=True, db_index=True)
    choice = models.CharField(max_length=2, verbose_name='25 cm оставить', choices=choice_status_2, default=true)
    category = models.ForeignKey(Caregory, verbose_name='категория', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Готовые окна'
        verbose_name_plural = 'Готовые окна'

    def __str__(self):
        return self.title


class WindowModel(models.Model):
    pm = 'PM'
    sht = 'ST'
    choice_status = [
        (pm, 'П.М'),
        (sht, 'ШТ')
    ]
    category = models.ForeignKey(Window, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name='продукция', on_delete=models.CASCADE, blank=True, default=True)
    measurement = models.CharField(max_length=2, verbose_name='единица измерения', choices=choice_status, default=pm)
    count = models.IntegerField('Каличество', default=0)
    price = models.DecimalField('цена', max_digits=100, decimal_places=2, default=0)

    # def __str__(self):
    #     return self.product


class Partner(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='partner', blank=True)
    place = models.IntegerField(default=0, unique=True)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ('place', )

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    grade = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)],
                                default=0)
    video = models.FileField(upload_to='review', null=True)
    created = models.DateTimeField(auto_now_add=True)
    uploded = models.DateTimeField(auto_now=True)
    place = models.IntegerField(default=0, unique=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('place',)

    def __str__(self):
        return self.name


class Pedestal(models.Model):
    title = models.CharField('', max_length=100)
    category = models.ForeignKey(Caregory, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField('Фото', upload_to='pedestal', blank=True, db_index=True)

    class Meta:
        verbose_name = 'Палястра'
        verbose_name_plural = 'Палястры'

    def __str__(self):
        return self.title


class PedestalModel(models.Model):
    pm = 'PM'
    sht = 'ST'
    choice_status = [
        (pm, 'П.М'),
        (sht, 'ШТ')
    ]
    category = models.ForeignKey(Pedestal, on_delete=models.CASCADE, null=True, blank=True)
    poster = models.ImageField('Размер', upload_to='pedestal/model', blank=True, db_index=True)
    title = models.CharField('наименование', max_length=100)
    measurement = models.CharField(max_length=2, verbose_name='единица измерения', choices=choice_status, default=pm)
    count = models.IntegerField('Каличество', default=0)
    size_1 = models.IntegerField('размер')
    size_2 = models.IntegerField('размер')


