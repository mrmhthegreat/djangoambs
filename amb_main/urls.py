
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dataentery.urls")),
    path("", home, name="name"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
