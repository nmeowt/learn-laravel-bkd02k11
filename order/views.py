from django.http.response import JsonResponse
from django.shortcuts import render
from cart.cart import Cart

# Create your views here.


def order_create(request):
    cart = Cart(request)
    # if request.method == 'POST':
    #     form = OrderCreateForm(request.POST)
    #     if form.is_valid():
    #         order = form.save()
    #         for item in cart:
    #             OrderItem.objects.create(order=order,
    #                                      customer=request.user.profile.username,
    #                                      product=item['product'],
    #                                      price=item['price'],
    #                                      calories=item['product'].calories,
    #                                      quantity=item['quantity'])
    #             import pdb
    #             pdb.set_trace()
    #         # clear the cart
    #         cart.clear()
    #         order_created(order.id)
    #         request.session['order_id'] = order.id
    #         # import pdb
    #         # pdb.set_trace()
    #         customer_user = User.objects.get(username='sb_owner')
    #         notify.send(request.user, recipient=customer_user, actor=request.user,
    #                     verb='placed an order', nf_type='followed_by_one_user')
    #         # redirect to the payment
    #         return redirect('shop:product_list')
    #         # return redirect('payment:process')

    # else:
    #     form = OrderCreateForm()
    # return render(request,
    #               'orders/create.html',
    #               {'cart': cart, 'form': form})
    return JsonResponse({"hello": "world"})
