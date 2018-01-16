from django.db import models
from django.contrib.auth.models import User

default_image_path = 'img/default.jpg'

class Flight(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    flight_number = models.CharField(max_length=50, default='0000')
    airlines = models.CharField(max_length=50, default='default airlines')
    image_url = models.CharField(default=default_image_path, max_length=256, null=False)
    description = models.CharField(max_length=500, default='default flight description')
    airplane = models.CharField(max_length=50, default='default airplane')
    departure_airport = models.CharField(max_length=50, default='DFL')
    arrival_airport = models.CharField(max_length=3, default='DFL')
    cost = models.CharField(max_length=20, default='99999 рублей')
    participation = models.ManyToManyField(User)

    class Meta():
        db_table = 'flights'