# Generated by Django 4.0.6 on 2022-07-07 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='place',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='place',
            field=models.IntegerField(default=0),
        ),
    ]