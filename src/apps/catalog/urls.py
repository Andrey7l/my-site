from django.urls import path

from apps.catalog.views import view_catalog

urlpatterns = [
path('', view_catalog, name= "catalog"),]