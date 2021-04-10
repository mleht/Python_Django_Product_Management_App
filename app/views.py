from django.shortcuts import render
from .models import Supplier, Product

def landingview(request):
    return render (request, "landingpage.html")

def supplierlistview(request):
    supplierlist = Supplier.objects.all() # haetaan kaikki 
    context = {'suppliers': supplierlist}
    return render (request, "suppliers.html", context)

def productlistview(request):
    productlist = Product.objects.all() # haetaan kaikki
    context = {'products': productlist}
    return render (request, "products.html", context)
