from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Category(models.Model):
    c_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    discription=models.CharField(max_length=300)
    c_images=models.ImageField(upload_to='category',default='default_image.jpg')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.c_name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.c_name


class Fooditem(models.Model):
    food_name=models.CharField(max_length=100,unique=True)
    c_name=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    discription=models.CharField(max_length=120)
    f_image=models.ImageField(upload_to='food',default='default_image.jpg')
    price=models.IntegerField()
    rating=models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(5.0)])

    def __str__(self):
        return self.food_name
    
class Review(models.Model):
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    rating=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    comments=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class reserve(models.Model):
    seats=models.IntegerField()
   
class reservedetails(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    date=models.DateField()
    time=models.CharField(max_length=20)
    no_guest=models.IntegerField()
    def __str__(self):
        return self.name


