from django.shortcuts import render
from webapp.models import brands,product
# Create your views here.
def products(request):
    products=product.objects.all()
    brand=brands.objects.all()
    return render(request,'products.html',{'products':products,'brands':brand})