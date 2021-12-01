from .models import *
from .views import *


def cats(request):
    ct=Category.objects.all()
    return dict(cats=ct)
        
