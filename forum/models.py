from django.db import models
from django.contrib.auth.models import User


class Topics(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    topic_name = models.CharField(max_length=250)
    topic_desc = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class Posts(models.Model):
    post_id = models.IntegerField(primary_key=True)
    post_name = models.CharField(max_length=250)
    post_desc = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    parent_topic = models.ForeignKey(Topics, on_delete=models.CASCADE, default=None)


class Comments(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    comment_name = models.CharField(max_length=250)
    comment_desc = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    parent_post = models.ForeignKey(Posts, on_delete=models.CASCADE, default=None)

