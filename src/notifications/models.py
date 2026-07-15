import uuid

from django.db import models


class APIKey(models.Model):
    prefix = models.CharField()
    hashed_key = models.CharField(primary_key=True)
    service_name = models.CharField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(
        "APIKey", on_delete=models.CASCADE, to_field="hashed_key"
    )
    channel = models.CharField()
    recipient = models.CharField()
    payload = models.JSONField()
    status = models.CharField(
        choices=[
            ("pending", "Pending"),
            ("sent", "Sent"),
            ("failed", "Failed"),
            ("invalid", "Invalid"),
        ],
        default="pending",
    )
    # Populated if status is INVALID - stores what was expected vs received
    error_details = models.JSONField(null=True, default=None)
    # Stores the raw response/error from SendGrid/Twilio
    provider_response = models.JSONField(null=True)
    # unique constraint combined with the client
    idempotency_key = models.CharField(null=True)
    retry_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, default=None)
    update_at = models.DateTimeField(auto_now=True)
