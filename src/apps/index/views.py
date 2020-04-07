from django.http import HttpRequest
from django.shortcuts import render


def view_index(request: HttpRequest):
    return render (request, "index/index.html")


