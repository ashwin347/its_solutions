from django.shortcuts import render
from django.http import HttpResponse
import os
import json
from webapp.models import product,services,brands
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def index(request):
    file=os.path.join(BASE_DIR,'/static/main.json')
    f = open (file ,"r")
    info=json.loads(f.read())
    products=product.objects.all()
    allservices=services.objects.all()
    allbrands=brands.objects.all()
    return render(request,'index.html',{'products':products,'services':allservices,'brands':allbrands,'info':info})
