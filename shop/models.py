from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Caregory(models.Model):
    title = models.CharField('название', max_length=100, db_index=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField('наименование', max_length=100)
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

    class Meta:
        ordering = ('id', )
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


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


class Window(models.Model):
    title = models.CharField('Названия', max_length=100, default='')
    # code_product = models.CharField('Код продукта', max_length=100, default='')
    descriptions = models.TextField(max_length=1000, default='')
    available = models.BooleanField('наличие', default=True)
    image = models.ImageField('Фото', upload_to='window', blank=True, db_index=True)
    category = models.ForeignKey(Caregory, verbose_name='категория', on_delete=models.CASCADE,
                                 null=True, related_name='category')

    class Meta:
        verbose_name = 'Готовые окна'
        verbose_name_plural = 'Готовые окна'
        ordering = ('id', )

    def __str__(self):
        return self.title


class WindowModel(models.Model):
    choice_status = [
        ('PM', 'П.М'),
        ('ST', 'ШТ')
    ]
    choice_status_1 = [
        ('dn', 'нижний часть'),
        ('wh', 'верхний часть'),
        ('dw', 'верхний и нижный часть'),
        ('bk', 'бокавые части'),
        ('dl', 'деталь')
    ]
    choice_status_2 = [
        ('true', 'Да'),
        ('false', 'Нет'),
    ]
    category = models.ForeignKey(Window, related_name='window', on_delete=models.CASCADE, default=0)
    choice = models.CharField(max_length=5, verbose_name='Часть', choices=choice_status_1, default='dn')
    product = models.ForeignKey(Product, verbose_name='продукция', on_delete=models.CASCADE, default='')
    measurement = models.CharField(max_length=2, verbose_name='единица измерения', choices=choice_status, default='PM')
    count = models. IntegerField('каличество', default=0, null=True)
    choice_window = models.CharField(max_length=5, verbose_name='25 cm оставить', choices=choice_status_2, default='false')

    class Meta:
        verbose_name = 'Экземпляр'
        verbose_name_plural = 'Экзепляры'

    def __str__(self):
        return f'{self.product}'


class Pedestal(models.Model):
    title = models.CharField('Наименование', max_length=100)
    category = models.ForeignKey(Caregory, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField('Фото', upload_to='pedestal', blank=True, db_index=True)
    descriptions = models.TextField(max_length=1000, default='')
    available = models.BooleanField('наличие', default=True)

    class Meta:
        verbose_name = 'Стойка'
        verbose_name_plural = 'Стойка'
        ordering = ('id', )

    def __str__(self):
        return self.title


class PedestalModel(models.Model):
    choice_status = [
        ('PM', 'П.М'),
        ('SHT', 'ШТ'),
    ]
    choice_status_1 = [
        ('angular', 'наименование угловой'),
        ('facial', 'наименование лицовой'),
        ('name', 'наименование'),
    ]
    choice_status_2 = [
        ('top', 'Верхний часть'),
        ('average', 'Средний часть'),
        ('lower', 'Нижный часть'),
        ('top and lower', 'Верхний и нижный часть'),
    ]
    category = models.ForeignKey(Pedestal, on_delete=models.CASCADE, null=True, blank=True, related_name='rack')
    poster = models.ImageField('Размер', upload_to='pedestal/model', blank=True, db_index=True)
    title = models.CharField('наименование', max_length=100)
    choice = models.CharField(max_length=10, verbose_name='', choices=choice_status_1, default='angular')
    measurement = models.CharField(max_length=10, verbose_name='единица измерения', choices=choice_status, default='PM')
    choice_1 = models.CharField(max_length=20, verbose_name='часть', choices=choice_status_2, default='top')
    size_1 = models.IntegerField('размер')
    price_pm = models.DecimalField('цена за ШТ', max_digits=100, decimal_places=2, default=0)
    price_sht = models.DecimalField('цена за П.М', max_digits=100, decimal_places=2, default=0)
    size_2 = models.IntegerField('размер', null=True, default=0)
    price_2 = models.DecimalField('цена за ШТ или П.М', max_digits=100, decimal_places=2, null=True, default=0)
    available = models.BooleanField('Если два размера', default=False)

    class Meta:
        verbose_name = 'Тумба'
        verbose_name_plural = 'Тумбы'

    def __str__(self):
        return self.title



