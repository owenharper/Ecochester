from django.contrib import admin
from django.urls import path

from . import views

app_name = "forum"  # Namespace for fourm app used to resolve urls using resolve()

urlpatterns = [
    path('', views.index, name='index'),
    path("example_post", views.chat_post, name="example_post"),
    path("<str:topic_name>", views.topic_page),
    path("<str:topic_name>/<str:post_name>", views.post_page),
]