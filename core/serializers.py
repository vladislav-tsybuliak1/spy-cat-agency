from rest_framework import serializers

from core.models import (
    SpyCat,
)


class SpyCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ("id", "name", "years_of_experience", "breed", "salary")
