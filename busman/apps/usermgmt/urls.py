from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import IndexView
from .forms import AuthenticateForm

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(template_name="usermgmt/login.html",
                                     authentication_form=AuthenticateForm), name="login"),
    path('logout/', LogoutView.as_view(template_name="usermgmt/logged_out.html"))
]
