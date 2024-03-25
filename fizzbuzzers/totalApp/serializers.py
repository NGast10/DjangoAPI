from .models import fizzBuzz
from rest_framework import serializers
#Creates the serializer that allows data types to be easily converted
class fizzBuzzSerializer(serializers.ModelSerializer):
	class Meta:
		model = fizzBuzz
		fields = ("id", "userAgent", "creationDate", "message")
