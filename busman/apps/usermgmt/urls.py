from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import IndexView, CustomLoginView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name="usermgmt/logged_out.html"))
]
