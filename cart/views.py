from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def cart_details(request,t=0,tot=0,count=0,ct_items=None):
    try:
        ct=Cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart_id=ct,active=True)
        for i in ct_items:
            item_total=0
            t=i.product.total_price()
            tot += t*i.quantity
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    
    return render(request,'cart_page.html',{'total':tot,'cart_items':ct_items,'total_quantity':count})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod=Product.objects.get(id=product_id)
    try:
        ct=Cartlist.objects.get(cart_id=c_id(request))
    except Cartlist.DoesNotExist:
        ct=Cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(cart_id=ct,product=prod)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity += 1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(cart_id=ct,product=prod,quantity=1)
        c_items.save()
    return redirect('cartdetails')

def min_cart(request,product_id):
    ct=Cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(Product,id=product_id)
    c_items=items.objects.get(product=prod,cart_id=ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')
    
def cart_delete(request,product_id):
    ct=Cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(Product,id=product_id)
    c_items=items.objects.get(product=prod,cart_id=ct)
    c_items.delete()
    return redirect('cartdetails')

def checkout(request,t=0,tot=0,count=0,ct_items=None):
    try:
        ct=Cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart_id=ct,active=True)
        for i in ct_items:
            item_total=0
            t=i.product.total_price()
            tot += t*i.quantity
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'checkout.html',{'total':tot,'cart_items':ct_items,'total_quantity':count})

def check_out(request,product_id):
    prod=Product.objects.get(id=product_id)
    return render(request,'check_out.html',{'item':prod})
