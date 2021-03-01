from .models import Item
from django.shortcuts import render, redirect
from .new_item_form import ItemForm
from .search_form import SearchForm
from trade_search.models import Hub
from trade_search.views import trade_search
from django.urls import reverse
from django.core.serializers import serialize



list_item="tradeshop.html"

def all_items(request):
	#replace tradeshop.html with whatever
    return render(request,list_item,{'Item':Item.objects.all()})

def my_item(request):
	if request.user.is_authenticated:
		#replace tradeshop.html with whatever
		return render(request, list_item, {'Item':Item.objects.filter(user=request.user)})
	else:
		return redirect(reverse('login', args={}))

def item_name(request):
	#replace name if necessary
	if request.method == 'GET' and request.GET['name']!="":
		#replace tradeshop.html with view items
		return render(request,list_item,{"Item":Item.objects.filter(itemname=request.GET['name'])})
	else:
		return render(request,list_item,{"Item":Item.objects.all()})

def click_item(request,value=None):
	if request.method=='GET':
		#replace speicific_item with whatever
		return render(request,"specific_item.html",{"Item":Item.objects.get(itemid=int(value))})

def item_hub(request):
	form=SearchForm(request.GET)
	chosenhub=form.cleaned_data['chosen_hub']
	return render(request,list_item,{"Item":Item.objects.filter(hub=chosenhub)})

def register_item(request):
	hubs = serialize('json', Hub.objects.all())
	context = {"form": ItemForm(), "results": [], "hubs": hubs}
	if request.method == 'POST':
		if request.user.is_authenticated:
			form = ItemForm(request.POST)
			if form.is_valid():
				instance=form.save(commit=False)
				instance.user=request.user
				instance.save()
				return redirect(reverse('login', args={}))
				#Change this to a page which views created item
			else:
				return (render(request, "Item/item_registration.html", context))
		else:
			return redirect(reverse('login', args={}))
	else:
		return (render(request, "Item/item_registration.html", context))