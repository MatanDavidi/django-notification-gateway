# Input/Output validation & representation
from rest_framework.serializers import ModelSerializer

from .models import Notification


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            "id",
            "client",
            "channel",
            "recipient",
            "payload",
            "status",
            "error_details",
            "provider_response",
            "idempotency_key",
            "retry_count",
            "created_at",
            "sent_at",
            "update_at",
        )
