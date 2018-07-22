from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Route
from .utils import serialize_state


@method_decorator(login_required, name="dispatch")
class MapView(TemplateView):
    template_name = "busmap/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = serialize_state(self.request)
        return context
