from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import product,services,brands
import os
import json
# Create your views here.
def basicinfo(request):
    return render(request,"basicinfo.html")
def tables(request):
    products=product.objects.all()
    allservices=services.objects.all()
    allbrands=brands.objects.all()
    return render(request,'admin.html',{'products':products,'services':allservices,'brands':allbrands})
def add(request):
    if request.GET.get('table')=='product':
        productname=request.GET.get('product')
        subtitle=request.GET.get('subtitle')
        desc=request.GET.get('desc')
        brand=brands.objects.get(id=request.GET.get('brand'))
        service=services.objects.get(id=request.GET.get('service'))
        product(productname=productname,subtitle=subtitle,desc=desc,brand=brand,services=service,featured=True,popular=True).save()
        return HttpResponse("success")
def delete(request):
    table=request.GET.get('table')
    idval=request.GET.get('id')
    if(table=="products"):
        product.objects.get(id=idval).delete()
    if(table=="brands"):
        brands.objects.get(id=idval).delete()
    if(table=="services"):
        services.objects.get(id=idval).delete()
    return HttpResponse("success")
