from django.contrib import admin
from entity.models import (ImageTag, Organization, OrganizationClassification,
                           OrganizationImage, Person, PersonImage)

admin.site.register(ImageTag)
admin.site.register(Organization)
admin.site.register(OrganizationImage)
admin.site.register(OrganizationClassification)
admin.site.register(Person)
admin.site.register(PersonImage)
