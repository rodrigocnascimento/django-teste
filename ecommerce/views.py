from django.contrib import messages
from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegistrationForm, UpdateUserPasswordForm, UpdateUserForm, LoginForm, CheckoutForm
from product.models import Product, Sale
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def register_page(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso :)")
            return redirect('ecommerce:home_ecommerce')
        else:
            messages.warning(request, "Existem erros no formulário.")
            return redirect(request, 'ecommerce/register.html', {'form': form})

    form = RegistrationForm()
    return render(request, 'ecommerce/register.html', {'form': form})


def user_profile(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.POST:
        form = UpdateUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro editado com sucesso :)")
        else:
            messages.warning(request, "Existem erros no formulário.")

        return render(request, 'ecommerce/user_profile.html', {'form': form})
    else:
        form = UpdateUserForm(instance=user)
        return render(request, 'ecommerce/user_profile.html', {'form': form})


def change_password(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.POST:
        form = UpdateUserPasswordForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('ecommerce:dashboard_ecommerce')
        else:
            messages.warning(request, "Existem erros no formulário.")
            return render(request, 'ecommerce/change_password.html', {'form': form})
    else:
        form = UpdateUserPasswordForm(instance=user)
        return render(request, 'ecommerce/change_password.html', {'form': form})


def login_ecommerce(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')

    return render(request, 'ecommerce/login.html', {'form': form})


def logout_ecommerce(request):
    logout(request)
    return HttpResponseRedirect('/')


def home_ecommerce(request):
    products = Product.objects.all().exclude(user_id=request.user.id)
    return render(request, 'ecommerce/home.html', {'products': products})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'ecommerce/product_detail.html', {'product': product})


@login_required(login_url='/login/')
def dashboard_ecommerce(request):
    user_id = request.user.id
    user_sold_items = Sale.get_user_selled_items(Sale, user_id)
    user_bought_items = Sale.get_user_bought_items(Sale, user_id)
    return render(request, 'ecommerce/dashboard.html',
                  {'user_sold_items': user_sold_items, 'user_bought_items': user_bought_items})


@login_required(login_url='/login/')
def checkout(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.POST:
        data = request.POST
        seller = get_object_or_404(User, pk=product.user_id)
        buyer = request.user
        # Update quantity product
        Product.objects.update(product_qtd=F('product_qtd') - data['sale_product_qtd'])
        # Update sales object
        sale = Sale.objects.create(product=product, buyer=buyer, seller=seller,
                                   sale_product_price=product.product_price,
                                   sale_product_qtd=data['sale_product_qtd'])
        sale.save()

        messages.success(request, 'Parabéns! Produto comprado com sucesso :)')
        return HttpResponseRedirect('/')

    form = CheckoutForm()
    return render(request, 'ecommerce/checkout.html', {'form': form, 'product': product})
