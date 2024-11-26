from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import SpyCatViewSet, MissionViewSet

router = DefaultRouter()
router.register("cats", SpyCatViewSet)
router.register("missions", MissionViewSet)

urlpatterns = router.urls

app_name = "core"
