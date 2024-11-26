from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import (
    SpyCat,
)


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ("id", "name", "years_of_experience", "breed", "salary")


class SpyCatCreateSerializer(SpyCatSerializer):
    def validate(self, attrs: dict) -> dict:
        data = super().validate(attrs=attrs)
        SpyCat.validate_breed_name(
            breed=attrs.get("breed"),
            error_to_raise=ValidationError,
        )
        return data
