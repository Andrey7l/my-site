from pathlib import Path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path



here = Path(__file__).parent.resolve()
def view(r):
    index = here.parent.parent / "index.html"
    with index.open() as f:
        return HttpResponse(f.read())
def fon(r):
    index = here.parent.parent / "fon_st1.jpg"
    with index.open("rb") as f:
        return HttpResponse(f.read(), content_type="image/jpg")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path('fon_st1.jpg', fon),
]