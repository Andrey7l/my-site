from pathlib import Path
from django.contrib import admin
from django.urls import path, include

from apps.catalog.views import view_catalog

here = Path(__file__).parent.resolve()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.index.urls")),
    path('catalog/', include("apps.catalog.urls")),
]