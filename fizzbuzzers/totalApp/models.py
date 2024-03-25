from django.db import models
from django.utils import timezone
#creating the model for the fizzbuzzes
class fizzBuzz(models.Model):
	id = models.CharField(primary_key=True,max_length=1)
	userAgent = models.CharField(max_length=165)
	creationDate = models.DateTimeField(default=timezone.now)
	message = models.CharField(max_length=50)

	def __str__(self):
		return self.id


		# Create your models here.
