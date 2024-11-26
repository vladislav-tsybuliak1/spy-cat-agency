from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import (
    SpyCat,
    Target,
    Mission,
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


class SpyCatUpdateSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ("salary",)


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ("id", "name", "country", "notes", "is_complete")


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(
        many=True,
        read_only=False,
        allow_empty=False,
    )

    class Meta:
        model = Mission
        fields = ("id", "assigned_cat", "is_complete", "targets")
