from django.views.generic import TemplateView
from django.shortcuts import render


class LoginView(TemplateView):
    template_name = "page_base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Login'
        return context
