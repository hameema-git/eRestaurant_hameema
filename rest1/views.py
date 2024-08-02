from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Category,Fooditem,Review,reserve,reservedetails
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest1.forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'aboutus.html')

@login_required
def home(request):
    return render(request,'home.html')

def register_view(request):
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("successfully registered")
            return redirect(reverse('login'))
    return render(request,'register.html',{'form':form})
def login(request):
    return render(request,'registration/login.html')

def menu(request):
    cat_dict={
        'cat':Category.objects.all()
    }
    return render(request,'menu.html',cat_dict)

def Food(request):
    food_dict={
        'food':Fooditem.objects.all()
                }
    return render(request,'items.html',food_dict)

from django.shortcuts import render,get_object_or_404
def food_list(request,c_name_slug=None):
    categories=Category.objects.all()
    foods=Fooditem.objects.all()

    if c_name_slug:
        category=get_object_or_404(Category,slug=c_name_slug)
        foods=foods.filter(c_name=category)
    else:
        category=None

    context={
        'category':category,
        'categories':categories,
        'foods':foods,
    }
    return render(request,'items.html',context)

def reviews(request):
    rev_dict={
        'rev':Review.objects.all(),
       
    }
    return render(request,'viewreview.html',rev_dict)

def createrev(request):
    if request.method=='GET':
        return render(request,'createreview.html')
    elif request.method=='POST':
        name=request.POST['name']
        place=request.POST['place']
        rating=request.POST['rating']
        comment=request.POST['comment']
    rev1=Review(name=name,place=place,rating=rating,comments=comment)
    rev1.save()
    rev_dict={
        'rev':Review.objects.all()
    }
    return render(request,'viewreview.html',rev_dict)
def reservation1(request):
    res_dict={
        'res':reserve.objects.all()
    }
    return render(request,'reservation.html',res_dict)

def reservation(request):

    if request.method=='GET':
        return render(request,'reservecreate.html')
    elif request.method=='POST':
        seats1=request.POST['bs']
        obj=reserve.objects.all()
        old=obj[0].seats
        obj.delete()
        seats=old-int(seats1)
    # return HttpResponse(seats)
    res1=reserve(seats=str(seats))
    res1.save()
    res_dict={
        'res':reserve.objects.all()
    }
    return redirect('pg7')
    return render(request,'reservecreate.html',res_dict)  
    # res1=reserve(seats=seats)
    # res1.save()
    # res_dict={
    #     'res':reserve.objects.filter(id=1)
    # }
    # return render(request,'reservation.html',res_dict)

def reservedetail(request):
    if request.method=='GET':
        return render(request,'reservedetails.html')
    elif request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        date=request.POST['date']
        time=request.POST['time']
        no_guest=request.POST['nq']
    rev1=reservedetails(name=name,phone=phone,date=date,time=time,no_guest=no_guest)
    rev1.save()
    # rev_dict={
    #     'rev':reservedetails.objects.all()
    # }
    messages.success(request, 'successfully reserved table')
    return render(request,'message.html')

def cart(request):
    return render(request,'cart.html')