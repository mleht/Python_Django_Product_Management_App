from django.urls import path
from .views import landingview, supplierlistview, addsupplier, productlistview, addproduct, deletesupplier, deleteproduct, edit_product_get, edit_product_post, edit_supplier_get, edit_supplier_post #eli importoidaan saman kansion views.py tiedostosta

urlpatterns = [
    path('', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
]
# Sovelluksen juuressa näytetään landingview