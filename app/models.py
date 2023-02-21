from django.db import models

# Create your models here.
class Soccer(models.Model):
    gps_data = models.CharField(max_length=100)
    time_stamp = models.DateTimeField()
    player_name = models.CharField(max_length=100)
    player_id = models.IntegerField()
    player_tshirt_number = models.IntegerField()

class Stadium(models.Model):
    c1 = models.CharField(max_length=100)
    c2 = models.CharField(max_length=100)
    c3 = models.CharField(max_length=100)
    c4 = models.CharField(max_length=100)