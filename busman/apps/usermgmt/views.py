from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import AuthenticateForm


class IndexView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse("You're logged in {}".format(request.user.username))
        else:
            return redirect('login')
