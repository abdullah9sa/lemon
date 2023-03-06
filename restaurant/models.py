from django.db import models

# Create your models here.
class menu(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField()


class booking(models.Model):
    tableno = models.IntegerField()
    persons = models.IntegerField()   