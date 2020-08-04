from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactInfo
import json
from django.core import serializers

# To access the api data
# Endpoint : http://127.0.0.1:8000/
# json.map(dog => dog['fields']['data']['pets']['dogs'])

def home(request):
	dogs = ContactInfo.objects.all()

	dogs_json = serializers.serialize('json',dogs)
	dogs_obj = json.loads(dogs_json)
	return HttpResponse(json.dumps(dogs_obj))