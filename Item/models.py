from django.db import models

# Create your models here.
class Item(models.Model):
    itemid = models.AutoField(primary_key=True)
    itemname=models.TextField()
    description=models.TextField()
    created_at=models.DateField()
    image=models.ImageField()
    country_code=models.TextField()


