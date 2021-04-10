from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default = 'Oy Firma Ab')
    contactname = models.CharField(max_length = 50, default = 'Aku')
    address = models.CharField(max_length = 100, default = 'Paratiisitie 13')
    phone = models.CharField(max_length = 20, default = '313313')
    email = models.CharField(max_length = 50, default = 'aku@ankka.com')
    country = models.CharField(max_length = 20, default = 'Finland')
    objects = models.Manager() # pylint luuleman virheilmoituksen poistamiseen - ei välttämätön

class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "Auton rengas")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    unitsinstock = models.IntegerField(default = 3)
    companyname = models.CharField(max_length = 50, default = 'Oy Firma Ab')
    objects = models.Manager() # pylint luuleman virheilmoituksen poistamiseen - ei välttämätön
