from django.urls import path
from . import views


urlpatterns=[
    path('cartdetails',views.cart_details,name='cartdetails'),
    path('add_cart/<int:product_id>',views.add_cart,name='add_cart'),
    path('dec_cart/<int:product_id>',views.min_cart,name='decrement'),
    path('cart_delete/<int:product_id>',views.cart_delete,name='delete'),
    path('checkout',views.checkout,name='checkout'),
    path('check_out/<int:product_id>',views.check_out,name='check_out'),
    ]
