from django.db import models



# Create your models here.
class Hub(models.Model):
	name = models.CharField(max_length = 40)
	other_info = models.TextField(blank = True)
	latitude = models.FloatField()
	longitude = models.FloatField()


	def __str__(self):
		return self.name