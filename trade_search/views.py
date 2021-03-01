from django.shortcuts import render
from .search_form import SearchForm
from .models import Hub
from Item.models import Item
from django.core.serializers import serialize

# Create your views here.
def trade_search(request):
	hubs = serialize('json', Hub.objects.all())
	context = {"blank_form": SearchForm(), "results": [], "hubs": hubs}
	form = SearchForm(request.GET)
	if form.is_valid():
		context["results"] += Item.objects.filter(hub = form.cleaned_data["chosen_hub"])
		context["results"].append("no more results")
		context["results"].append(form.cleaned_data["chosen_hub"])
		return (render(request, "trade_search/trade_search.html", context))
	else:
		return (render(request, "trade_search/trade_search.html", context))