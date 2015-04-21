from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=128, unique=True)
    device_range = models.IntegerField(default=0)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name





