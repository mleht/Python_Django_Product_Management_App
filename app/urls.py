from django.urls import path
from .views import landingview, supplierlistview, addsupplier, productlistview, addproduct, deletesupplier, deleteproduct, edit_product_get, edit_product_post #eli importoidaan saman kansion views.py tiedostosta

urlpatterns = [
    path('', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
]
# Sovelluksen juuressa näytetään landingview