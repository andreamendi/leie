from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = request.user
        print(user.product_set.all())
        user_product = user.product_set.all()
        context = {
            'products': user_product
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')

def detail_product(request, product_id):
    user = request.user
    product = user.product_set.get(id=product_id)
    context ={
        'product': product
    }
    return render(request, 'detail.html', context)


        
# def hola(request, name):
#     return HttpResponse('{}'.format(name))