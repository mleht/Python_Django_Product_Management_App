from django.urls import path
from .views import landingview #eli importoidaan saman kansion views.py tiedostosta

urlpatterns = [
    path('', landingview),
]
# Sovelluksen juuressa näytetään landingview