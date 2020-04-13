from django.http import HttpRequest
from django.shortcuts import render


#def view_catalog (request: HttpRequest):
#return render(request, "catalog/catalog.html")
from django.views import View
from django.views.generic import TemplateView


class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"

# def get(self, request):
#   return render(request, "catalog/catalog.html")