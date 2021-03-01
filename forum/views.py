from django.shortcuts import render
from django.http import HttpResponse
from .models import Topics
from .models import Posts
from .models import Comments
from users.models import Profile
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    # return HttpResponse('<h1>this is the forum homepage<h1>')
    topics = list(Topics.objects.all())
    user_list = []
    for topic in topics:
        user_list.append(str(topic.author))
    for x in range(len(user_list)):
        user_obj = User.objects.filter(username=user_list[x])
        for user in user_obj:
            user_list[x] = user.pk

    users = list(Profile.objects.filter(user__in=user_list))
    context = {
        'topics': topics,
        'users': users,
        'topics_users': zip(topics, users)

    }
    return render(request, "forumMain.html", context)


def topic_page(request, topic_name):
    topic = Topics.objects.get(topic_name=topic_name)
    topic_id = int(topic.topic_id)
    Posts_obj = Posts.objects.filter(parent_topic_id=topic_id)
    context = {
        'topic': topic,
        'posts': Posts_obj,
    }
    return render(request, "forum_topic_thread.html", context)


def post_page(request, post_name, topic_name):
    post_name, topic_name = post_name.replace('-', ' '), topic_name.replace('-', ' ')
    post = Posts.objects.get(post_name=post_name)
    post_id = int(post.post_id)
    Comments_obj = Comments.objects.filter(parent_post=post_id)
    context = {
        'post': post,
        'comments': Comments_obj,
    }
    return render(request, "forum_post.html", context)


def chat_post(request):
    return render(request, "forum_post.html", {})
