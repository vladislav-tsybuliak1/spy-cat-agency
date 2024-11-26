from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import SpyCat
from core.serializers import (
    SpyCatSerializer,
    SpyCatCreateSerializer,
    SpyCatUpdateSalarySerializer,
)


class SpyCatViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    def get_serializer_class(self) -> type[SpyCatSerializer]:
        if self.action == "create":
            return SpyCatCreateSerializer
        return self.serializer_class

    @action(
        methods=["PATCH"],
        detail=True,
        url_path="update-salary",
    )
    def update_salary(self, request: Request, pk: int | None = None) -> Response:
        spy_cat = self.get_object()
        serializer = SpyCatUpdateSalarySerializer(
            spy_cat,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            SpyCatSerializer(spy_cat).data,
            status=status.HTTP_200_OK,
        )
