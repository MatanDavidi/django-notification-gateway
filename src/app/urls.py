from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authentication import SessionAuthentication

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "docs/schema.yml",
        SpectacularAPIView.as_view(
            permission_classes=[],
            authentication_classes=[SessionAuthentication],
        ),
        name="schema",
    ),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema",
            permission_classes=[],
            authentication_classes=[SessionAuthentication],
        ),
        name="swagger-ui",
    ),
    path(
        "api/v1/notifications/",
        include("notifications.urls", namespace="notifications"),
    ),
]
