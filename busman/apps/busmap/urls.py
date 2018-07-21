from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import MapView

urlpatterns = [
    path('', MapView.as_view(), name="busmap"),
]
