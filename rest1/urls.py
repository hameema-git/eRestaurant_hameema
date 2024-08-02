from .views import *
from django.urls import path,include
from . import views
urlpatterns = [
    path("home/",home,name='pg1'),
    path("menu/",menu,name='pg2'),
    path('product/',food_list,name='pg'),
    path('product/<slug:c_name_slug>/',food_list,name='food_list_by_category'),
    path('product/<slug:slug>/',Food,name='product_detail'),
    path("review1/" ,reviews,name='pg3'),
    path("crereview/",createrev,name='pg4'),
    path('reserve/',reservation1,name='pg5'),
    path('reserveform/',reservation,name='pg6'),
    path('reservdetail/',reservedetail,name='pg7'),
    path("cart/",cart,name="pg8"),
    path("register/",views.register_view,name='register'),
    path("register/",register_view,name="pg9"),
    path("",login,name='login'),
    path("about/",about,name="pg10")
    
]

