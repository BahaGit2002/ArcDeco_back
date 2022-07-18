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
    pm = 'PM'
    sht = 'ST'
    true = 'tr'
    false = 'fa'
    choice_status = [
        (pm, 'П.М'),
        (sht, 'ШТ')
    ]
    choice_status_2 = [
        (true, 'Да'),
        (false, 'Нет')
    ]
    image = models.ImageField(upload_to='window', blank=True)
    # category = models.ManyToManyField(Caregory, verbose_name='категория', blank=True)
    product = models.ForeignKey(Product, verbose_name='продукция', on_delete=models.CASCADE, blank=True, default=True)
    measurement = models.CharField(max_length=2, verbose_name='единица измерения', choices=choice_status, default=pm)
    count = models.IntegerField('Каличество')
    price = models.DecimalField('цена', max_digits=100, decimal_places=2)
    product_detail = models.ManyToManyField(Product, verbose_name='продукция для деталя', blank=True)
    measurement_detail = models.CharField(max_length=2, verbose_name='единица измерения для деталя', choices=choice_status, default=pm)
    count_detail = models.IntegerField('Каличество для деталя')
    price_detail = models.DecimalField('цена для деталя', max_digits=100, decimal_places=2)
    choice = models.CharField(max_length=2, verbose_name='25см оставить', choices=choice_status_2, default=true)

    class Meta:
        verbose_name = 'Готовые окна'
        verbose_name_plural = 'Готовые окна'


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

    # def save(self, *args, **kwargs):
    #     grade = Review.objects.all().aggregate(Avg('grade'))
    #     if args != () and kwargs != ():
    #         super(Review, self).save()
    #     print(args)
    #     return grade
