from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(6)
    booking_date = models.DateField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    inventory = models.IntegerField(5)
    price = models.IntegerField()
