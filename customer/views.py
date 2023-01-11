from django.shortcuts import render,redirect
from common.models import Customer
from seller.models import Product
from .models import Cart


# Create your views here.

def change_password(request):
    error_msg = ''
    success_msg = ''
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if len(new_password) > 8:
                customer = Customer.objects.get(id = request.session['customer'])
                if old_password == customer.password:
                    Customer.objects.filter(id = request.session['customer']).update(password = new_password)
                   
                    success_msg = 'updated successfully'
                else:
                    error_msg = 'Invalid password'    

            else:
                error_msg = 'Password should be minimum 8 characters'
        
        else :
            error_msg = 'password does\'nt  match'
    



    return render(request,'customer/change password.html',{'success':success_msg,'error':error_msg})


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

def productdetails(request,pid):
    product_details = Product.objects.get(id = pid)
    msg = ''
    if request.method == 'POST':
        item = Cart.objects.filter(customer = request.session['customer'],product = pid).exists()
        if not item:           #same as if item == false:

            cart_item = Cart(customer_id = request.session['customer'],product_id = pid)
            cart_item.save()
            return redirect('customer:cart')
        else:
            msg = 'Item already in cart'


    return render(request,'customer/productdetails.html',{'details':product_details,'message':msg})
    

def profile(request):
    return render(request,'customer/profile.html')   

def mycart(request): 

    return render(request,'customer/mycart.html')     
