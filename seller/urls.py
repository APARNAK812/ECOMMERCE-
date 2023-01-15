from django.urls import path
from.import views
app_name = 'seller'

urlpatterns=[
    path('add_product',views.add_product ,name='add_product'),
    path('home',views.home, name= 'home'),
    path('product_catalogue',views.product_catalogue,name='catalogue'),
    path('profile',views.profile ,name='profile'),
    path('profile_update',views.profile_update ,name='profile_update'),
    path('update_stocks',views.update_stocks,name='stocks'),
    path('view_order',views.view_order),
    path('master',views.master),
    path('change_password',views.change_password,name='password'),
    path('update_stocks',views.update_stocks,name='stocks'),
    path('stock_number',views.stock_number,name='stock_number')
]