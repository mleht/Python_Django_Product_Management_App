from django.shortcuts import render, redirect
from .models import Supplier, Product
from django.contrib.auth import authenticate, login, logout

def landingview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        return render (request, "landingpage.html")

#login & logout
def loginview(request):
    return render (request, "loginpage.html")

def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username = user, password = passw)
    if user:
        login(request, user)
        mydictionary = {'name' : user}
        return render(request, 'landingpage.html', context=mydictionary)
    else:
        return render(request, 'loginerror.html')

def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

#suppliers
def supplierlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplierlist = Supplier.objects.all() # haetaan kaikki 
        mydictionary = {'suppliers': supplierlist} # Tähän dictionaryn 'suppliers' viitataan suppliers.html for-loopissa
        return render (request, "suppliers.html", context=mydictionary)

def addsupplier(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['companyname']
        b = request.POST['contactname']
        c = request.POST['address']
        d = request.POST['phone']
        e = request.POST['email']
        f = request.POST['country']
        Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
        return redirect(request.META['HTTP_REFERER'])    
    # Formilta tulee tiedot a, b jne. ja niillä luodaan modelin mukainen Supplier, joka tallennetaan heti
    # request.POST  Only handles form data.  Only works for 'POST' method. - https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
    # HTTP_REFERER – The referring page, (if any)
    # HttpRequest.META: A dictionary containing all available HTTP headers : https://docs.djangoproject.com/en/3.1/ref/request-response/


def deletesupplier(request,id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Supplier.objects.filter(id = id).delete() # deletoidaan se supplier, jonka id on sama kuin parametrina saatu (jälkimmäinen on parametri)
        return redirect(request.META['HTTP_REFERER'])

def edit_supplier_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplier = Supplier.objects.filter(id = id)
        mydictionary = {'supplier': supplier}
        return render (request,"edit_supplier.html",context=mydictionary)

def edit_supplier_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        item = Supplier.objects.get(id = id)
        item.companyname = request.POST['companyname']
        item.contactname = request.POST['contactname']
        item.address = request.POST['address']
        item.phone = request.POST['phone']
        item.email = request.POST['email']
        item.country = request.POST['country']
        item.save()
        return redirect(supplierlistview)

#products
def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all() # haetaan kaikki
        mydictionary = {'products': productlist} # Tähän dictionaryn 'products' viitataan products.html for-loopissa
        return render (request, "products.html", context=mydictionary)

def addproduct(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['companyname']
        Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, companyname = e).save()
        return redirect(request.META['HTTP_REFERER'])
    # Formilta tulee tiedot a, b jne. ja niillä luodaan modelin mukainen Product, joka tallennetaan heti
    # request.POST  Only handles form data.  Only works for 'POST' method. - https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
    # HTTP_REFERER – The referring page, (if any)
    # HttpRequest.META: A dictionary containing all available HTTP headers : https://docs.djangoproject.com/en/3.1/ref/request-response/

def deleteproduct(request,id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Product.objects.filter(id = id).delete() #deletoidaan se tuote, jonka id on sama kuin parametrina saatu id (jälkimmäinen on parametri)
        return redirect(request.META['HTTP_REFERER'])

def edit_product_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        product = Product.objects.filter(id = id)
        mydictionary = {'product': product}
        return render (request,"edit_product.html", context=mydictionary)

def edit_product_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        item = Product.objects.get(id = id)
        item.productname = request.POST['productname']
        item.packagesize = request.POST['packagesize']
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.companyname = request.POST['companyname']
        item.save()
        return redirect(productlistview)

def products_by_supplier(request,id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplierObj = Supplier.objects.get(id = id)
        company = supplierObj.companyname
        productlist = Product.objects.all()
        filteredproducts = productlist.filter(companyname = company)
        mydictionary = {'products':filteredproducts}
        return render (request,"products.html", context=mydictionary)
