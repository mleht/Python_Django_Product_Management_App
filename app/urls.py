from django.urls import path
from .views import landingview, supplierlistview, addsupplier, productlistview, addproduct, deletesupplier, deleteproduct #eli importoidaan saman kansion views.py tiedostosta

urlpatterns = [
    path('', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
]
# Sovelluksen juuressa näytetään landingview