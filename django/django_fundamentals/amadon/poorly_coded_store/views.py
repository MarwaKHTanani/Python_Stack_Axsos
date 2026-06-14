from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum


def index(request):
    context = {"all_products": Product.objects.all()}
    return render(request, "store/index.html", context)


def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id=request.POST["product_id"])
    price = product.price
    total_charge = quantity_from_form * price
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("/checkout/result")


def checkout_page(request):
    last_order = Order.objects.last()
    context = {
        "last_order_total": last_order.total_price if last_order else 0,
        "total_items": Order.objects.aggregate(Sum("quantity_ordered"))[
            "quantity_ordered__sum"
        ],
        "total_amount": Order.objects.aggregate(Sum("total_price"))["total_price__sum"],
    }
    return render(request, "store/checkout.html", context)
