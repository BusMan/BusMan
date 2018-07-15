from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.views import LoginView

from .forms import AuthenticateForm


class CustomLoginView(LoginView):
    template_name = "usermgmt/login.html"
    authentication_form = AuthenticateForm
    extra_context = {
        "data": {
            "school": settings.SCHOOL
        }
    }


class IndexView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse("You're logged in {}".format(request.user.username))
        else:
            return redirect('login')
