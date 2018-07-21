from django.shortcuts import render
from django.views.generic import TemplateView


class MapView(TemplateView):
    template_name = "busmap/map.html"
