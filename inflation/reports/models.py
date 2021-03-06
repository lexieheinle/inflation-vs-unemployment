from django.db import models
from datetime import datetime

# Create your models here.
class Inflation(models.Model):
    """Model class to create Inflation objects with rate, date"""
    rate = models.FloatField(null=True)
    date = models.DateField()
  
    def __str__(self):
        """Return user friendly Model representation"""
        return "{0} on {1}".format(self.rate, self.date)
  
    def get_absolute_url(self):
        """Return Model absolute url"""
        return "/inflation/{0}/".format(datetime.strftime(self.date, "%Y/%m"))


class Unemployment(models.Model):
    """Model class to create Unemployment objects with rate, date"""
    rate = models.FloatField(null=True)
    date = models.DateField()
  
    def __str__(self):
        """Return user friendly Model representation"""
        return "{0} on {1}".format(self.rate, self.date)
  
    def get_absolute_url(self):
        """Return Model absolute url"""
        return "/unemployment/{0}".format(datetime.strftime(self.date, "%Y/%m"))

class Interest(models.Model):
    """Model class to create Interest objects with rate, date"""
    rate = models.FloatField(null=True)
    date = models.DateField()
  
    def __str__(self):
        """Return user friendly Model representation"""
        return "{0} on {1}".format(self.rate, self.date)
  
    def get_absolute_url(self):
        """Return Model absolute url"""
        return "/interest/{0}".format(datetime.strftime(self.date, "%Y/%m"))