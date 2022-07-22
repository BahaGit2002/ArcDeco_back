# Generated by Django 4.0.6 on 2022-07-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0040_rename_category_1_windowmodel_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedestalmodel',
            options={'verbose_name': 'Тумба', 'verbose_name_plural': 'Тумбы'},
        ),
        migrations.RemoveField(
            model_name='window',
            name='choice',
        ),
        migrations.AddField(
            model_name='windowmodel',
            name='choice_window',
            field=models.CharField(choices=[('true', 'Да'), ('false', 'Нет')], default='true', max_length=5, verbose_name='25 cm оставить'),
        ),
    ]