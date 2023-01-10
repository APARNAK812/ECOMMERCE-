from django.urls import path
from.import views
app_name='customer'
urlpatterns=[
    path('change_password',views.change_password,name='password'),
    path('checkout',views.checkout,name='check'),
    path('home',views.home,name='home'),
    path('myorders',views.myorders,name='orders'), 
    path('productdetails',views.productdetails,name='details'), 
    path('profile',views.profile,name='pro'),
    path('mycart',views.mycart,name='cart'),
]