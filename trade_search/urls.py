from django.urls import path
from . import views

urlpatterns = [
	path('', views.trade_search, name = 'trade_search'),
]