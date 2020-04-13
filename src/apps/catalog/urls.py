from django.urls import path

#from apps.catalog.views import view_catalog
from apps.catalog.views import CatalogView

urlpatterns = [
    path('', CatalogView.as_view(), name="catalog"),
]