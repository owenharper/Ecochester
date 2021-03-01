from django.urls import path

from . import views


urlpatterns = [
    path('', views.register_item, name='register_item'),
]