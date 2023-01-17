from django.shortcuts import render,redirect
from common.models import Seller
from .models import Product
from django.http import JsonResponse

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
    products = Product.objects.filter(seller_id = request.session['seller'])
    seller_pic = seller_details.seller_pic
    sname = seller_details.first_name + ' ' + seller_details.last_name
    context = {
        'seller':seller_details,   
        'products' :products,
        'name' : sname 
         }
    
    return render(request,'seller/home.html',context)
     

def product_catalogue(request):
    return render(request,'seller/product catalogue.html') 

def master(request):
    return render(request,'seller/master.html')   

def profile(request):
    seller_details = Seller.objects.get(id=request.session['seller'])
    return render(request,'seller/profile.html',{'profile':seller_details})

def profile_update(request):
    msg = ''
    
    if request.method  == "POST":
        msg = 'updated successfully'
        new_name = request.POST['new_name']
        last_name = request.POST['last_name']
        new_address = request.POST['address']
        new_phone = request.POST['phone']
        image = request.FILES['image']
        
        seller = Seller.objects.get(id =request.session['seller'])
        # print(seller.id)
        seller.seller_pic = image
        seller.first_name = new_name
        seller.last_name = last_name
        seller.address = new_address
        seller.phone = new_phone
        # update = Seller(seller_pic = image,first_name = new_name,last_name = last_name,address = new_address,phone = new_phone)
        seller.save()
    profile_update = Seller.objects.get(id = request.session['seller'])
    return render(request,'seller/profile_update.html',{'profile_update':profile_update,'msg':msg}) 
    


def view_order(request):
    return render(request,'seller/view order.html')  

def change_password(request):
    error_msg = ''
    success_msg = ''
    if request.method  == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if len(new_password) > 8:
                seller = Seller.objects.get(id = request.session['seller'])
                if old_password == seller.password:
                    seller.password = new_password
                    seller.save()
                    success_msg = 'updated successfully'
                else:
                    error_msg = 'Invalid password'    

            else:
                error_msg = 'Password should be minimum 8 characters'
        
        else :
            error_msg = 'password does\'nt  match'
    

    return render(request,'seller/change password.html',{'error':error_msg,'success':success_msg})        


def update_stocks(request):
    product = Product.objects.filter(seller_id =request.session['seller'])
    if request.method == 'POST':
        prodid =request.POST['pid']
        print(prodid)
        new_stock =request.POST['new_stock']
        product1 =Product.objects.get(id=prodid)
        product1.stock += int(new_stock)
        product1.save()
    return render(request,'seller/update_stocks.html',{'products':product})



def stock_number(request):
    qty = request.POST['qty']
    product = Product.objects.filter(id=qty).values('product_name','stock')
    p_name = product[0]['product_name']
    p_stock = product[0]['stock']
    return JsonResponse({'pname':p_name,'pstock':p_stock})
    
def logout(request):
    del request.session['seller'] 
    request.session.flush()
    return redirect('common:home')   
      