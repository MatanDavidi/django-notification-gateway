# NotificationService (Domain Logic / Orchestration)
from rest_framework import mixins, viewsets


class NotificationService:
    @classmethod
    def dispatch(cls, api_key_instance, raw_payload: dict, idempotency_key: str = None):
        """
        Entrypoint for new notifications.
        1. Checks idempotency_key + client constraint. If exists, return existing.
        2. Validates raw_payload.
        3. If invalid: creates INVALID Notification, raises exception.
        4. If valid: creates PENDING Notification, delegates to _send().
        """
