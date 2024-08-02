# Generated by Django 5.0.6 on 2024-07-29 05:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest1', '0003_fooditem_c_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='rating',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]