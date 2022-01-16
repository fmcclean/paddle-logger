from django.db import models

# Create your models here.


class River(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    url = models.URLField()


class Paddle(models.Model):
    id = models.AutoField(primary_key=True)
    river = models.ForeignKey(River, on_delete=models.SET_NULL, null=True)
    level = models.FloatField()
    date = models.DateField()
    description = models.TextField()
