from django.shortcuts import render, redirect
from .models import Supplier, Product

def landingview(request):
    return render (request, "landingpage.html")

def supplierlistview(request):
    supplierlist = Supplier.objects.all() # haetaan kaikki 
    mydictionary = {'suppliers': supplierlist} # Tähän dictionaryn 'suppliers' viitataan suppliers.html for-loopissa
    return render (request, "suppliers.html", context=mydictionary)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])    
    # Formilta tulee tiedot a, b jne. ja niillä luodaam modelin mukainen Supplier, joka tallennetaan heti
    # request.POST  Only handles form data.  Only works for 'POST' method. - https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
    # HTTP_REFERER – The referring page, (if any)
    # HttpRequest.META: A dictionary containing all available HTTP headers : https://docs.djangoproject.com/en/3.1/ref/request-response/

def productlistview(request):
    productlist = Product.objects.all() # haetaan kaikki
    mydictionary = {'products': productlist} # Tähän dictionaryn 'products' viitataan products.html for-loopissa
    return render (request, "products.html", context=mydictionary)
