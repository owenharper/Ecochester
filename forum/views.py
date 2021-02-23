from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    #return HttpResponse('<h1>this is the forum homepage<h1>')
    return render(request, "forumMain.html", {})

def chat_post(request):
	return render(request, "forum_post.html", {})
