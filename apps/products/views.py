# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from .models import Product, ProductSellPrice
# from .forms import ProductSearchForm, ProductForm
# from apps.Users.permissions import user_is_admin


# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

# # View for creating a new product
# @method_decorator([login_required, user_is_admin], name='dispatch')
# def create_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.seller = request.user  # Set the seller to the logged-in user
#             product.save()
#             return redirect('products:product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'products/create_product.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, ProductSellPrice
from .forms import ProductForm, ProductSearchForm
from apps.Users.permissions import user_is_admin

# View for creating a new product
@login_required
@user_is_admin
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # Set the seller to the logged-in user
            product.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/create_product.html', {'form': form})



def product_list(request):
    products = Product.objects.all()
    seller_price = ProductSellPrice.objects.all()
    return render(request, "products/product_list.html", {"products": products})

def product_search(request):
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.all()
    if form.is_valid():
        query = form.cleaned_data.get("query")
        if query:
            products = products.filter(title__icontains=query)
    return render(request, "products/product_search.html", {"form": form, "products": products})


def add_product_price(request, product):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('products:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/add_product_price.html', {'form': form, 'product': product})
