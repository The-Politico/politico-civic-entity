from entity.models import Person
from entity.serializers import PersonSerializer, SlimPersonSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == 'list':
            return SlimPersonSerializer
        else:
            return PersonSerializer
