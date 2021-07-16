from django.db import models
from django.contrib.gis.db import models as gis_models

from providers.utils import phone_number_validator


class Providers(models.Model):
    """
    Provider model store the service provider details
    """
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    # International Phone Number support with country code and + sign
    phone_number = models.CharField(validators=[phone_number_validator],
                                    max_length=16,
                                    unique=True)
    # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    language = models.CharField(max_length=3)
    # https://en.wikipedia.org/wiki/ISO_4217
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class ServiceAreas(gis_models.Model):
    """
    ServiceAreas store the information
    of the providers multiple service locations in Polygon geojson

    """
    provider = models.ForeignKey(Providers, on_delete=models.CASCADE)
    polygon_name = models.CharField(max_length=255)
    price = models.FloatField()
    # GeoDjango-specific: a geometry field with Multi Polygon accept
    polygon = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.polygon_name
