# Thin controller endpoints (Create, Retry, Health, etc.)
from notifications.models import Notification
from notifications.serializers import NotificationSerializer
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet


class NotificationViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
