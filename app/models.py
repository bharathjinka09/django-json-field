from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    data = models.JSONField()

    def __str__(self):
    	return str(self.data)