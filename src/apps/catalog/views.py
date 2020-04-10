from django.http import HttpRequest
from django.shortcuts import render


def view_catalog (request: HttpRequest):
    return render(request, "catalog/catalog.html")