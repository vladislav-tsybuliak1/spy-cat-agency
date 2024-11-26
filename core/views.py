from rest_framework import viewsets

from core.models import SpyCat
from core.serializers import SpyCatSerializer, SpyCatCreateSerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    def get_serializer_class(self) -> type[SpyCatSerializer]:
        if self.action in ["create"]:
            return SpyCatCreateSerializer
        return self.serializer_class
