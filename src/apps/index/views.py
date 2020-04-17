from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


# def view_index(request: HttpRequest):
#   if request.method == "GET":
#    return render (request, "index/index.html")
from django.views.generic import TemplateView

from apps.index.models import UserInfo

#fff
class IndexView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        info = UserInfo.objects.first()
        ctr = {"name" : info.name, "greeting": info.greeting}

        ctr.update(parent_ctx)

        return ctr
# super() обращение к самому себе только что относится к TemplateView
        # обращение метода от родителя

# def get(self, request):
#     return render(request, "index/index.html")