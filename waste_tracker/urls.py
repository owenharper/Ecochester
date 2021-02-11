from django.urls import path
from waste_tracker import views
from .views import line_chart, line_chart_json

urlpatterns = [
	path('', views.line_chart, name="line_chart.html"),
	path('chart', line_chart, name='line_chart'),
	path('chartJSON', line_chart_json, name='line_chart_json'),
]