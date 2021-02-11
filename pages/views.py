from django.shortcuts import render
from django.http import HttpResponse
from Item.models import Item


# Create your views here.
def trade_view(request,*args, **kwargs):
    objs={
        "Items":Item.objects.all(),
    }

    return render(request,"tradeshop.html",objs)