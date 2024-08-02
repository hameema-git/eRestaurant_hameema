from django.contrib import admin
from .models import Category,Fooditem,Review,reserve,reservedetails
# Register your models here.
admin.site.register(Category)
admin.site.register(Fooditem)
admin.site.register(Review)
admin.site.register(reserve)
admin.site.register(reservedetails)