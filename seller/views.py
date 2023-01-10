from django.shortcuts import render
from common.models import Seller
from .models import Product

# Create your views here.


def add_product(request):
    if request.method  == "POST":
        category = request.POST['category']
        product_name = request.POST['product_name']
        product_no = request.POST['product_no']
        product_description = request.POST['product_description']
        price = request.POST['price']
        stock = request.POST['stock']
        image = request.FILES['image']
        seller = request.session['seller']
        new_product = Product(category = category,product_name = product_name,product_no = product_no ,

        product_description = product_description, price = price,stock = stock, image = image, seller_id=seller)
        new_product.save() 

    return render(request,'seller/add product.html')

def home(request):
    seller_details = Seller.objects.get(id = request.session['seller'])
    seller_pic = seller_details.seller_pic
    sname = seller_details.first_name + ' ' + seller_details.last_name
    
    return render(request,'seller/home.html',{'name':sname, 'image':seller_pic})
     

def product_catalogue(request):
    return render(request,'seller/product catalogue.html')    

def profile(request):
    return render(request,'seller/profile.html')

def update_stocks(request):
    return render(request,'seller/update stocks.html')  

def view_order(request):
    return render(request,'seller/view order.html')  

def change_password(request):
    return render(request,'seller/change password.html')        