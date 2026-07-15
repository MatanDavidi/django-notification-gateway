# App-specific URL routing
from django.urls import include
from notifications.views import NotificationViewSet
from rest_framework.routers import DefaultRouter, re_path

router = DefaultRouter()
router.register("notification", NotificationViewSet, basename="notification")

urlpatterns = [re_path("^", include(router.urls))]
