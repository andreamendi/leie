from django.shortcuts import render, redirect
from django.http import HttpResponse
from .froms import ProductForm
from .models import Product


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

def create_product(request):
    if request.user.is_authenticated:
        form = ProductForm(request.POST or None)
        if request.method == 'POST':
            
            if form.is_valid():
                product = form.save(commit = False)
                product.user = request.user
                product.save()
                return redirect('index') 

        return render(request, 'product_create.html', {'form': form})
    else:
        return redirect('login')


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
          
                product = form.save(commit = False)
                product.save()
                return redirect('index')     
        else:

            form = ProductForm(instance=product)
        return render(request, 'update_product.html', {'form': form})
            
    else:
        return redirect('login')
