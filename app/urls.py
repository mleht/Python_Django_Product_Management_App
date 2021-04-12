from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.landingview, name='landingview'),

    #login
    path('', views.loginview, name ='loginview'),
    path('login/', views.login_action, name='login_action'),
    path('logout/', views.logout_action, name='logout_action'),

    #suppliers
    path('suppliers/', views.supplierlistview, name='suppliers'),
    path('add-supplier/', views.addsupplier, name='add-supplier'),
    path('delete-supplier/<int:id>/', views.deletesupplier, name='delete-supplier'),
    path('edit-supplier-get/<int:id>/', views.edit_supplier_get, name='edit-supplier-get'),
    path('edit-supplier-post/<int:id>/', views.edit_supplier_post, name='edit-supplier-post'),

    #products
    path('products/', views.productlistview, name='products'),
    path('add-product/', views.addproduct, name='add-product'),
    path('delete-product/<int:id>/', views.deleteproduct, name='delete-product'),
    path('edit-product-get/<int:id>/', views.edit_product_get, name='edit-product-get'),
    path('edit-product-post/<int:id>/', views.edit_product_post, name='edit-product-post'),
    path('products-by-supplier/<int:id>/', views.products_by_supplier, name='products-by-supplier'),
]
# Sovelluksen juuressa näytetään landingview