from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/', views.home, name='product_category'),
    path('<slug:c_slug>/<slug:product_slug>', views.product_details, name='details'),
    path('hot-deals',views.deals,name='deals'),
    path('hotdeals/<slug:ct_slug>/',views.deals,name='deals_on'),
    path('search',views.search,name="search"),
    path('product_category',views.product_cat,name='products'),
    path('<slug:c_slug>',views.product_cat,name='product'),
    ]
