from .models import *
from .views import *


def count(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            tot=0
            ct=Cartlist.objects.filter(cart_id=c_id(request))
            ct_i=items.objects.all().filter(cart_id=ct[:1])
            for i in ct_i:
                item_count+=i.quantity
                tot+=i.product.total_price()*i.quantity
        except Cartlist.DoesNotExist:
            item_count=0
        return dict(itc=item_count,t=tot)
        
