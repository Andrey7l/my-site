from pathlib import Path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


here = Path(__file__).parent.resolve()
def view(r):
    index = here.parent.parent / "index.html"
    with index.open() as f:
        return HttpResponse(f.read())
def foto(r):
    index = here.parent.parent / "foto.jpg"
    with index.open("rb") as f:
        return HttpResponse(src.read(), content_type="image/jpeg")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path('foto.jpg', foto),
]