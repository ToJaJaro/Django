from django.db import models

# Create your models here.
class MyModel(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=True)
