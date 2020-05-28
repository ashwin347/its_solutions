from django.shortcuts import render
from django.http import HttpResponse
import os
import json
from webapp.models import product,services,brands
def index(request):
    f = open ('static/main.json', "r")
    info=json.loads(f.read())
    products=product.objects.all()
    allservices=services.objects.all()
    allbrands=brands.objects.all()
    return render(request,'index.html',{'products':products,'services':allservices,'brands':allbrands,'info':info})
