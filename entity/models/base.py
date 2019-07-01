# flake8: noqa
# Imports from python.
import uuid


# Imports from Django.
from django.db import models


class NaturalKeyManager(models.Manager):
    def get_by_natural_key(self, *args):
        natural_key_fields = self.model.natural_key_fields

        if len(natural_key_fields) == len(args):
            natural_kwargs = dict(
                (field_name, queried_value)
                for field_name, queried_value in zip(natural_key_fields, args)
            )
            return self.get(**natural_kwargs)

        raise TypeError('Mismatched number of args and natural-key fields.')


class CommonIdentifiersMixin(models.Model):
    class Meta:
        abstract = True

    uid = models.CharField(
        max_length=500,
        editable=False,
        blank=True
    )

    slug = models.SlugField(
        blank=True, max_length=255, unique=True, editable=False
    )

    def generate_common_identifiers(self):
        """Generate slug and (if needed) UID field values."""
        self.slug = uuslug(
            getattr(self, self.slug_base_field),
            instance=self,
            max_length=100,
            separator='-',
            start_no=2
        )

        if not self.uid:
            self.uid = '{}:{}'.format(self.slug_prefix, self.slug)


class NaturalKeyMixin(models.Model):
    objects = NaturalKeyManager()

    class Meta:
        abstract = True

    natural_key_fields = []

    def get_natural_key_fields(self):
        """Override for self.natural_key_fields list, if needed."""
        return self.natural_key_fields

    def natural_key(self):
        return (
            self._meta.get_field(field)
            for field in self.get_natural_key_fields()
        )


class CivicBaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

    civic_version = (1, 0, 0)
