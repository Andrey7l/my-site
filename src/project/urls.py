from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from django.urls import path, include

from apps.index.views import view_index

here = Path(__file__).parent.resolve()



def fon(r):
    index = here.parent.parent / "fon_st1.jpg"
    with index.open("rb") as f:
        return HttpResponse(f.read(), content_type="image/jpg")

def view_contacts (request: HttpRequest):
    return render(request, "contacts.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.index.urls")),
    path('fon_st1.jpg', fon),
    path('contacts.html', view_contacts),
    path('index.html', include("apps.index.urls")),

]