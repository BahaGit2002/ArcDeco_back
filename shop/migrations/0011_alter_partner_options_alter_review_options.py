# Generated by Django 4.0.6 on 2022-07-08 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_partner_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ('place',), 'verbose_name': 'Партнер', 'verbose_name_plural': 'Партнеры'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('place',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]