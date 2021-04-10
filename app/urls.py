from django.urls import path
from .views import landingview, supplierlistview, addsupplier, productlistview, addproduct #eli importoidaan saman kansion views.py tiedostosta

urlpatterns = [
    path('', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('products/', productlistview),
    path('add-product/', addproduct),
]
# Sovelluksen juuressa näytetään landingview