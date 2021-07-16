from rest_framework import serializers
from rest_framework_gis.serializers import (GeoFeatureModelSerializer)

from providers.models import Providers, ServiceAreas


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Providers
        fields = '__all__'


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    """
    Serializer to return GeoJSON compatible format
    """

    class Meta:
        model = ServiceAreas
        geo_field = 'polygon'
        fields = '__all__'
