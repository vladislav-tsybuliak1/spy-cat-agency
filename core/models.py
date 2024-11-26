from django.db import models


class SpyCat(models.Model):
    name = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=63)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return str(self.name)


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
