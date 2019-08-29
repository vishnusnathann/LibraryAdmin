from django.db import models

# Create your models here.
class  Book(models.Model):
	book_name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	price = models.FloatField()
	avail=models.BooleanField(default=True)

	def __str__(self):
		return self.name