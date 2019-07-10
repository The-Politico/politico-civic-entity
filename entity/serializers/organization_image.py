# Imports from other dependencies.
from civic_utils.serializers import CommandLineListSerializer
from civic_utils.serializers import NaturalKeySerializerMixin
# from rest_framework import serializers


# Imports from entity.
from entity.models import OrganizationImage


class OrganizationImageSerializer(NaturalKeySerializerMixin,
                                  CommandLineListSerializer):
    class Meta(CommandLineListSerializer.Meta):
        model = OrganizationImage
        fields = (
            "created",
            "updated",
            "image",
        )
