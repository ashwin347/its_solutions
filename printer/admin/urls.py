
from django.urls import path
from . import views

urlpatterns = [
    path("tables",views.tables),
    path('basicinfo',views.basicinfo),
    path('add',views.add),
    path('delete',views.delete)
]
