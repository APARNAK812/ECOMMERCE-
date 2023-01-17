from django.shortcuts import render
from common.models import Seller
from common.models import Customer
from seller.models import Product


# Create your views here.


def approveseller(request):
    seller = Seller.objects.all()
    
    return render(request,'ecom_admin/approveseller.html',{'seller':seller})

def home(request):
    return render(request,'ecom_admin/home.html')    

def viewcustomer(request):
    customer = Customer.objects.all()
    return render(request,'ecom_admin/viewcustomer.html',{'customer':customer})

def viewseller(request):
    seller = Seller.objects.all()
    return render(request,'ecom_admin/viewseller.html',{'seller':seller}) 


def viewproduct(request):
    product = Product.objects.all()
    return render(request,'ecom_admin/viewproduct.html',{'product':product})  

def approval(request,sid):
    verify = Seller.objects.get(id = sid)
    verify.status = 'Approved'
    verify.save()