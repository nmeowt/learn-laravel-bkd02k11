import json
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from store.models import Product
from .cart import Cart


@require_POST
def cart_add(request):
    id_product = request.POST.get('id')
    quantity = int(request.POST.get('quantity'))
    update_quantity = True if request.POST.get('update_quantity') else False
    cart = Cart(request)
    product = get_object_or_404(Product, id=id_product)
    cart.add(product=product,
             quantity=quantity,
             update_quantity=update_quantity)
    return JsonResponse({
        "message": "Đã thêm vào giỏ hàng"
    })


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart-detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def cart_total_items(request):
    cart = Cart(request)
    print(cart.count())
    return JsonResponse({'cart': 'sss'})
