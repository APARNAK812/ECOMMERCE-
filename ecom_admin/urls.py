from django.urls import path
from.import views
app_name='ecom_admin'
urlpatterns=[
    path('approveseller<int:sid>',views.approveseller,name='approve_seller'),
    path('home',views.home,name='home'),
    path('viewcustomer',views.viewcustomer,name='view_cus'),
    path('viewseller',views.viewseller,name='view_sell'),
    path('viewproduct',views.viewproduct,name='view_product')
]
    