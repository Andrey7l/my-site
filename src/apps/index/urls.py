from django.urls import path

# from apps.index.views import view_index
from apps.index.views import IndexView

urlpatterns = [
    path('',  IndexView.as_view(), name="index"),
]
