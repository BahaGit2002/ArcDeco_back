from django.db import models


class ProductPortfolio(models.Model):
    title = models.CharField(max_length=200)
    pharetra = models.IntegerField()
    uorttitor = models.IntegerField()
    quisque = models.CharField(max_length=150)
    aliquet = models.IntegerField()
    poster = models.ImageField(upload_to='ProductPortfolio', blank=True)
    image1 = models.ImageField(upload_to='ProductPortfolio/image1', blank=True)
    image2 = models.ImageField(upload_to='ProductPortfolio/image2', blank=True)
    image3 = models.ImageField(upload_to='ProductPortfolio/image3', blank=True)
    discriptions = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    uploded = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар портфолии'
        verbose_name_plural = 'Товары портфолии'

    def __str__(self):
        return self.title



