from rest_framework import viewsets

from core.models import SpyCat
from core.serializers import SpyCateSerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCateSerializer
