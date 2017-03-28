from django.shortcuts import redirect
from .models import Product


def is_product_owner(function):
    def wrap(request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs['product_id'])
        if product.user_id == request.user.id:
            return function(request, *args, **kwargs)
        else:
            return redirect('product:index')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
