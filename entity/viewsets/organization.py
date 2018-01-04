from entity.models import Organization
from entity.serializers import (OrganizationSerializer,
                                SlimOrganizationSerializer)
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == 'list':
            return SlimOrganizationSerializer
        else:
            return OrganizationSerializer
