from django.db import models
class services(models.Model):
    servicename=models.TextField()
    servicedetail=models.TextField()
class brands(models.Model):
    brandname=models.TextField()
    brandimage=models.ImageField(upload_to="static/img/brands")
class bmodels(models.Model):
    bmodelname=models.TextField()
    brandname=models.ForeignKey(brands,on_delete=models.CASCADE)
class product(models.Model):
    productname=models.CharField(max_length=100)
    subtitle=models.TextField()
    desc=models.TextField()
    bmodel=models.ForeignKey(bmodels,null=True,on_delete=models.SET_NULL)
    brand=models.ForeignKey(brands,null=True,on_delete=models.SET_NULL)
    services=models.ForeignKey(services,null=True,on_delete=models.SET_NULL)
    productimage1=models.ImageField(upload_to='static/img/products',null=True)
    productimage2=models.ImageField(upload_to='static/img/products',null=True)
    productimage3=models.ImageField(upload_to='static/img/products',null=True)
    featured=models.BooleanField(default=False)
    popular=models.BooleanField(default=False)