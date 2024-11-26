from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import SpyCat, Mission
from core.serializers import (
    SpyCatSerializer,
    SpyCatCreateSerializer,
    SpyCatUpdateSalarySerializer,
    MissionSerializer,
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


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        instance = self.get_object()
        if instance.assigned_cat:
            return Response(
                {"detail": "Cannot delete a mission that is assigned to a cat."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
