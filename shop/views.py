from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Q
# Create your views here.

def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug is not None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products=Product.objects.filter(category=c_page,in_stock=True)
    else:
        products=Product.objects.all().filter(in_stock=True)
        
    categories=Category.objects.all()
    return render(request,'home.html',{'products':products,'categories':categories})

def product_details(request, c_slug, product_slug):
    try:
        pdt=Product.objects.get(category__slug=c_slug,slug=product_slug)
        pdt_ct=Product.objects.filter(category__slug=c_slug)
    except Exception as e:
        raise e

    return render(request,'product.html',{'product':pdt,'products_ct':pdt_ct})

def deals(request,ct_slug=None):
    c_page=None
    products=None
    if ct_slug is not None:
        c_page=get_object_or_404(Category,slug=ct_slug)
        products=Product.objects.filter(category=c_page,in_stock=True)
    else:
        products=Product.objects.all().filter(in_stock=True)
    categories=Category.objects.all()
    return render(request,'hotdeals.html',{'products':products,'categories':categories})

def search(request):
    prod = None
    query = None
    count=0
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=Product.objects.all().filter(Q(name__contains=query)| Q(description__contains=query))
        for p in prod:
            count+=1
        print(count)
    return render(request,'search.html',{'products':prod,'query':query,'count':count})
        
def product_cat(request,c_slug=None):
    print("success")
    pdts=None
    if c_slug is not None:
        pdts=Product.objects.filter(category__slug=c_slug)
    return render(request,'product_category.html',{'products':pdts})
