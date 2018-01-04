from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import OrganizationViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'organizations', OrganizationViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
