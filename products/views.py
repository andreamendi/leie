from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .froms import ProductForm
from .models import Product, Category, Rent
from django.contrib import messages

# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    if request.user.is_authenticated:
        user = request.user
        user_products = user.product_set.all()
        user_rents = user.rent_set.all()
        print(user_rents)
        context['products'] = user_products
        context['rents'] = user_rents
    return render(request, 'home.html', context)

def detail_product(request, product_id):
    user = request.user
    product = user.product_set.get(id=product_id)
    rents = []
    for rents in product:
        rents.append(product.rents.all())
    print(rents)
    context ={
        'product': product, 'rents': rents
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
                form.save_m2m()
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
          
                product = form.save()
                product.save()
                return redirect('index')     
        else:

            form = ProductForm(instance=product)
        return render(request, 'update_product.html', {'form': form})
            
    else:
        return redirect('login')


def delete_product(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk = product_id)
        product.delete()
        messages.add_message(request, messages.INFO, 'Product deleted')
        return redirect('index')
    return redirect('login')

