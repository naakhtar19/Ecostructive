from django.db import models

# Create your models here.
class Orders(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    category = models.CharField(max_length=200)
    timeslot = models.CharField(max_length=200)

    def __str__(self):
        return self.name
