# Generated by Django 4.0.6 on 2022-07-12 09:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_remove_review_star_review_grade_delete_reviewmiddle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=1, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'verbose_name': 'Звезда',
                'verbose_name_plural': 'Звезды',
            },
        ),
        migrations.RemoveField(
            model_name='review',
            name='grade',
        ),
        migrations.AddField(
            model_name='review',
            name='star',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.star'),
        ),
    ]