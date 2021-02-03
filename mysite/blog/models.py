from django.db import models

# Create your models here.

class Post(models.Model):

	title = models.CharField(max_length = 140)
	body  = models.TextField()
	date  = models.DateTimeField()

	# it will return the title in string rather than the post object
	def __str__(self):
		return self.title