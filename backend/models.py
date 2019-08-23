from django.db import models

class Data(models.Model):
    objects = models.Manager()
    tension = models.IntegerField()
    current = models.IntegerField()
    wind_speed = models.IntegerField()
    wind_direction = models.CharField(max_length = 20)

def __str__(self):
    return f'{self.tension}: {self.current} - {self.wind_speed}'