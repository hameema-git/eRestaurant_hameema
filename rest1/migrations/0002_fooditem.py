# Generated by Django 5.0.6 on 2024-07-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100, unique=True)),
                ('discription', models.CharField(max_length=120)),
                ('f_image', models.ImageField(default='default_image.jpg', upload_to='food')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
