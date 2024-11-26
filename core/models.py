from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from core.utils import get_valid_breeds


class SpyCat(models.Model):
    name = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=63)
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0.00")),
        ],
    )

    def __str__(self) -> str:
        return str(self.name)

    @staticmethod
    def validate_breed_name(breed: str, error_to_raise: type[Exception]):
        valid_breeds = get_valid_breeds()
        if breed not in valid_breeds:
            raise error_to_raise(f"{breed} is not a valid cat breed.")

    def clean(self) -> None:
        SpyCat.validate_breed_name(
            breed=str(self.breed),
            error_to_raise=ValidationError,
        )

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        super().save(*args, **kwargs)


class Mission(models.Model):
    assigned_cat = models.ForeignKey(
        to=SpyCat,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="missions",
    )
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Mission {self.pk} (Completed: {self.is_complete})"


class Target(models.Model):
    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE,
        related_name="targets",
    )
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=63)
    notes = models.TextField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.name)
