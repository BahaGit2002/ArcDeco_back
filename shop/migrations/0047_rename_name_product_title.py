# Generated by Django 4.0.6 on 2022-07-29 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0046_alter_pedestal_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
    ]
