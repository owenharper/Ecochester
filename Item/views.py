from django.shortcuts import render
from .models import Item
from django.shortcuts import render, redirect

def all_items(request):

    return render(request,"tradeshop.html",{'Item':Item.objects.all()})