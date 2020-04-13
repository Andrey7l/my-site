from pathlib import Path
from django.contrib import admin
from django.urls import path, include
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
#from apps.catalog.views import view_catalog

here = Path(__file__).parent.resolve()

def view_css(request: HttpRequest) -> HttpResponse:
    return render(request, "main.css")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.index.urls")),
    path('catalog/', include("apps.catalog.urls")),
    path('css/', view_css),
]