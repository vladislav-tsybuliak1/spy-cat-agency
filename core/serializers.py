from django.db import transaction
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

    def create(self, validated_data: dict) -> Mission:
        with transaction.atomic():
            targets_data = validated_data.pop("targets")
            if len(targets_data) > 3:
                raise ValidationError(
                    {
                        "detail": "The amount of targets for one mission should be less than 3!"
                    }
                )
            mission = Mission.objects.create(**validated_data)
            for target_data in targets_data:
                Target.objects.create(mission=mission, **target_data)
            return mission


class MissionListSerializer(MissionSerializer):
    targets = TargetSerializer(many=True, read_only=True)


class MissionRetrieveSerializer(MissionSerializer):
    targets = TargetSerializer(many=True, read_only=True)
    assigned_cat = SpyCatSerializer()


class AssignCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ("assigned_cat",)
