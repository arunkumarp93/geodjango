from django.contrib.gis import admin
from providers.models import Providers, ServiceAreas

admin.site.register(Providers)
admin.site.register(ServiceAreas, admin.OSMGeoAdmin)
