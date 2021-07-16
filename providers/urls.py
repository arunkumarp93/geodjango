from django.urls import path, include
from rest_framework.routers import DefaultRouter

from providers.views import (ProvidersViewSet, ServiceAreasViewSet,
                             ServiceAreaSearchView)

router = DefaultRouter()
router.register(r'providers', ProvidersViewSet)
router.register(r'serviceareas', ServiceAreasViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('search/', ServiceAreaSearchView.as_view())
]
