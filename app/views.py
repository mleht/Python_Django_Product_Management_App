from django.shortcuts import render
from .models import Supplier, Product

def landingview(request):
    return render (request, "landingpage.html")

def supplierlistview(request):
    supplierlist = Supplier.objects.all() # haetaan kaikki 
    mydictionary = {'suppliers': supplierlist} # Tähän dictionaryn 'suppliers' viitataan suppliers.html for-loopissa
    return render (request, "suppliers.html", context=mydictionary)

def productlistview(request):
    productlist = Product.objects.all() # haetaan kaikki
    mydictionary = {'products': productlist} # Tähän dictionaryn 'products' viitataan products.html for-loopissa
    return render (request, "products.html", context=mydictionary)
