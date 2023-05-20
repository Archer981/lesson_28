from django.contrib import admin
from django.urls import include, path

# TODO здесь можно подключить urls Ваших приложений

urlpatterns = [
    path("admin/", admin.site.urls),
    path("discount/", include("discounts.urls")),
    path("neva_tours/", include("along_neva_channels.urls")),
    path("", include("feedback.urls")),
    path("", include("forgotten.urls")),
    path("", include("moderation.urls")),
]
