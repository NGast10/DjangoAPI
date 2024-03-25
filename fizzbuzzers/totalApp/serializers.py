from .models import fizzBuzz
from rest_framework import serializers

class fizzBuzzSerializer(serializers.ModelSerializer):
	class Meta:
		model = fizzBuzz
		fields = ("id", "userAgent", "creationDate", "message")
