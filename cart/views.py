from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from store.models import Product
from .cart import Cart


@require_POST
def cart_add(request):
    id_product = request.POST.get('id')
    quantity = int(request.POST.get('quantity'))
    cart = Cart(request)
    product = get_object_or_404(Product, id=id_product)
    cart.add(product=product,
             quantity=quantity)
    return JsonResponse({
        "message": "Đã thêm vào giỏ hàng"
    })


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    # return redirect('cart:cart_detail')
    return JsonResponse({"foo": "bar"})


def cart_detail(request):
    cart = Cart(request)
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(
    #         initial={
    #             'quantity': item['quantity'],
    #             'update': True
    #         })
    # return render(request, 'cart/detail.html', {'cart': cart})
    return JsonResponse({"foo": "bar"})
