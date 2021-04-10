from django.urls import path
from .views import landingview, supplierlistview, addsupplier, productlistview #eli importoidaan saman kansion views.py tiedostosta

urlpatterns = [
    path('', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('products/', productlistview),
]
# Sovelluksen juuressa näytetään landingview