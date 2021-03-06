# Imports from python.
import os
import uuid


# Imports from Django.
from django.db import models
from django.utils.html import format_html


# Imports from politico-civic-entity.
from entity.models.base import CivicBaseModel
# from entity.models.base import NaturalKeyMixin
from entity.models.image_tag import ImageTag
from entity.models.person import Person


# Unfortunately, this is only around so the old migrations don't break
def person_image_path(instance, filename):
    return os.path.join(
        "cdn/images/people",
        instance.person.slug,
        "{}-{}{}".format(
            instance.tag,
            uuid.uuid4().hex[:6],
            os.path.splitext(filename)[1]
        ),
    )


class PersonImage(CivicBaseModel):
    """
    Image attached to a person, which can be serialized
    by a tag.
    """
    # NOTE: Subclassing CivicBaseModel would replace standard PK with a UUID.

    person = models.ForeignKey(
        Person,
        related_name="images",
        on_delete=models.PROTECT
    )
    tag = models.ForeignKey(
        ImageTag,
        related_name="+",
        on_delete=models.PROTECT,
        help_text="Used to serialize images.",
    )
    image = models.URLField()

    # created = models.DateTimeField(auto_now_add=True, editable=False)
    # updated = models.DateTimeField(auto_now=True, editable=False)

    def preview(self):
        return format_html(
            '<a href="{0}" target="_blank">'
            '<img src="{0}" style="max-height:100px; max-width: 300px;">'
            "</a>".format(self.image.url)
        )

    class Meta:
        unique_together = ("person", "tag")

    def __str__(self):
        return "{} {}".format(self.person.slug, self.tag.name)
