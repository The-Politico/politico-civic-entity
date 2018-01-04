from entity.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        """Object of images serialized by tag name."""
        return {str(i.tag.name): i.image.url for i in obj.images.all()}

    class Meta:
        model = Person
        fields = (
            'id',
            'uid',
            'slug',
            'last_name',
            'first_name',
            'middle_name',
            'suffix',
            'full_name',
            'identifiers',
            'gender',
            'race',
            'nationality',
            'state_of_residence',
            'birth_date',
            'death_date',
            'images',
            'summary',
            'biography',
            'links',
        )


class SlimPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
        )
