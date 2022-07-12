from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


class Caregory(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    width = models.IntegerField()
    height = models.IntegerField()
    category = models.ForeignKey(Caregory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', blank=True)
    poster1 = models.ImageField(upload_to='products/poster1', blank=True)
    poster2 = models.ImageField(upload_to='products/poster2', blank=True)
    poster3 = models.ImageField(upload_to='products/poster3', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    uploded = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default=0)

    class Meta:
        ordering = ('title', )
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


class Star(models.Model):
    grade = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)],
                                default=0)

    class Meta:
        verbose_name = 'Звезда'
        verbose_name_plural = 'Звезды'


class Review(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    star = models.ForeignKey(Star, related_name='star_choyses', on_delete=models.CASCADE, default=0)
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
