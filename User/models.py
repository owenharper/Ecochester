from django.db import models

# Create your models here.
class User():
    userid = models.AutoField(primary_key=True)
    username=models.TextField()
    email=models.EmailField()
    created_at=models.DateField()
    password=models.CharField(max_length=255)
    profile_image=models.ImageField()
    country_code=models.TextField()