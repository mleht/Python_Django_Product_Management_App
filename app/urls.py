from django.urls import path
from .views import landingview, supplierlistview, productlistview #eli importoidaan saman kansion views.py tiedostosta

urlpatterns = [
    path('', landingview),
    path('suppliers/', supplierlistview),
    path('products/', productlistview),
]
# Sovelluksen juuressa näytetään landingview