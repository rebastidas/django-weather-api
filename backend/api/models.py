from django.db import models

class CityWeather(models.Model):
    cityname = models.CharField(max_length=50, null=True, blank=True)
    currentemp = models.FloatField(null=True, blank=True)
    fellslike = models.FloatField(null=True, blank=True)
    averagetemp = models.IntegerField(null=True, blank=True)
    citylat = models.FloatField(null=True, blank=True)
    citylon = models.FloatField(null=True, blank=True)
    city_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.cityname