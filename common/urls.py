from django.urls import path
from.import views
app_name = 'common'

urlpatterns=[
    path('admin_logo',views.admin_logo),
    path('customer_login',views.customer_login),
    path('customer_signup',views.customer_signup),
    path('home',views.home),
    path('seller_login',views.seller_login),
    path('seller_signup',views.seller_signup),
]