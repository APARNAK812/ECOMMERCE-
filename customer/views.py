from django.shortcuts import render
from common.models import Customer
from seller.models import Product

# Create your views here.

def change_password(request):
    return render(request,'customer/change password.html')


def checkout(request):
    return render(request,'customer/checkout.html')

def home(request):
    customer_details = Customer.objects.get(id = request.session['customer'])
    products = Product.objects.all()
    cname = customer_details.first_name + ' ' + customer_details.last_name
    context = {
        'name':cname,
        'products':products

    }
    return render(request,'customer/home.html',context)    

def myorders(request):
    return render(request,'customer/myorders.html')    

def productdetails(request):
    return render(request,'customer/productdetails.html')

def profile(request):
    return render(request,'customer/profile.html')   

def mycart(request):
    return render(request,'customer/mycart.html')     
