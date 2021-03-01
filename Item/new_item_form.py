from django.forms import ModelForm
from trade_search.models import Hub
from .models import Item

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ["itemname", "description", "image", "hub"]
