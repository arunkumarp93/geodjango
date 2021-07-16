from rest_framework import viewsets, generics
from django.contrib.gis.geos import Point

from providers.models import Providers, ServiceAreas
from providers.serializers import (
    ProviderSerializer, ServiceAreaSerializer)


class ProvidersViewSet(viewsets.ModelViewSet):
    """
    Provider CRUD API
    """
    queryset = Providers.objects.order_by('name')
    serializer_class = ProviderSerializer
    partial = True


class ServiceAreasViewSet(viewsets.ModelViewSet):
    """
    Provider ServiceAreas CRUD API
    """
    queryset = ServiceAreas.objects.order_by('polygon_name')
    serializer_class = ServiceAreaSerializer
    partial = True


class ServiceAreaSearchView(generics.ListAPIView):
    """
    Provider search API
    """
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        """
        Returns the queryset of ServiceAreas that include the point
        given by `long` and `lat` parameters.
        """
        longitude = self.request.query_params.get('long', None)
        latitude = self.request.query_params.get('lat', None)

        if longitude is None or latitude is None:
            raise Exception('Need lat and long in the query params')

        try:
            long_pnt = float(longitude)
            lat_pnt = float(latitude)
        except (ValueError, TypeError):
            raise Exception(f'Invalid query params long = {longitude} lat={latitude}')

        point = Point(long_pnt, lat_pnt)
        return ServiceAreas.objects.filter(polygon__contains=point)
