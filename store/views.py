from .models import Category, Product
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-name')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'store/product-list.html', context)
