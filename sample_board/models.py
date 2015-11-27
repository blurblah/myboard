from django.db import models

# Create your models here.
class TestBoard(models.Model):
	title = models.CharField(max_length = 100)
	memo = models.CharField(max_length = 200)
	name = models.CharField(max_length = 50)
	created_date = models.DateField('date published')
	hits = models.IntegerField(default = 0)