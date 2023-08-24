from django.shortcuts import render

from .models import Order

# Create your views here.


def list_orders(request):
    orders = Order.objects.filter(positions__product__price__lte=600)
    context = {'orders': orders}
    return render(request, 'orders.html', context=context)