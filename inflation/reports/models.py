from django.db import models
from datetime import datetime

# Create your models here.
class Inflation(models.Model):
  rate = models.FloatField(null=True)
  date = models.DateField()
  
  def __str__(self):
    return "{0} on {1}".format(self.rate, self.date)
  
  def get_absolute_url(self):
    return "/inflation/{0}/".format(datetime.strftime(self.date, "%Y/%m"))


class Unemployment(models.Model):
  rate = models.FloatField(null=True)
  date = models.DateField()
  
  def __str__(self):
    return "{0} on {1}".format(self.rate, self.date)
  
  def get_absolute_url(self):
    return "/unemployment/{0}".format(datetime.strftime(self.date, "%Y/%m"))

class Interest(models.Model):
  rate = models.FloatField(null=True)
  date = models.DateField()
  
  def __str__(self):
    return "{0} on {1}".format(self.rate, self.date)
  
  def get_absolute_url(self):
    return "/interest/{0}".format(datetime.strftime(self.date, "%Y/%m"))