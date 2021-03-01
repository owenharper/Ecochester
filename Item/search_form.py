from django import forms
from .models import Hub

class SearchForm(forms.Form):
    min_value = forms.FloatField(help_text="Minimum value", required = False)
    max_value = forms.FloatField(help_text="Maximum value", required = False)
    chosen_hub = forms.ModelChoiceField(queryset = Hub.objects.all(), required = False, help_text="find a hub")