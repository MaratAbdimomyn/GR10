from django.db import models

class Town(models.Model):
    c_name = models.CharField(max_length=50)
    c_aeroport_index = models.CharField(max_length=50)
    c_car_number = models.CharField(max_length=50)

    def city_name(self):
        return self.c_name