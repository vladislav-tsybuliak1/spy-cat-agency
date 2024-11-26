from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import SpyCatViewSet


router = DefaultRouter()
router.register("cats", SpyCatViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "core"
