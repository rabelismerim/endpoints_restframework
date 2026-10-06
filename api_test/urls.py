from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="api-root", permanent=False)),
    path("api/polls/", include("polls.api.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]
