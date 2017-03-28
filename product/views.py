from django.shortcuts import render, redirect, get_object_or_404
from product.decorators import is_product_owner
from .models import Product
from .forms import ProductForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/login/')
def index(request):
    user = request.user
    products = Product.objects.all().filter(user_id=user.id)
    return render(request, 'product/index.html', {'products': products})


@login_required(login_url='/login/')
def add(request):
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user_id = request.user.id
            product.save()
            return redirect('product:index')
        else:
            messages.warning(request, 'Existem erros no formulário.')
            return render(request, 'product/add.html', {'form': form})

    form = ProductForm()
    return render(request, 'product/add.html', {'form': form})


@login_required(login_url='/login/')
@is_product_owner
def edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.POST:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product:index')
        else:
            messages.warning(request, 'Existem erros no formulário.')
            return render(request, 'product/edit.html', {'form': form, 'product_id': product_id})
    else:
        form = ProductForm(instance=product)

    return render(request, 'product/edit.html', {'form': form, 'product_id': product_id})


@login_required(login_url='/login/')
@is_product_owner
def delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    return redirect('product:index')
