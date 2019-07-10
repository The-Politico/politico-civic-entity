# Imports from other dependencies.
from civic_utils.serializers import CommandLineListSerializer
from civic_utils.serializers import NaturalKeySerializerMixin
# from rest_framework import serializers


# Imports from entity.
from entity.models import PersonImage


class PersonImageSerializer(NaturalKeySerializerMixin,
                            CommandLineListSerializer):
    class Meta(CommandLineListSerializer.Meta):
        model = PersonImage
        fields = (
            "created",
            "updated",
            "image",
        )
