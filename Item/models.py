from django.db import models
from django.contrib.auth.models import User
from trade_search.models import Hub
# Create your models here.
class Item(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner', null=True, editable = False)
    itemid = models.AutoField(primary_key=True)
    itemname=models.TextField()
    description=models.TextField(blank=True)
    created_at=models.DateField(auto_now=True)
    image=models.ImageField(blank=True)
    country_code=models.TextField(blank=True)
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE,null=True)