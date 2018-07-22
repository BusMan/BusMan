from .models import Route


def serialize_state(request):
    routes = Route.objects.all()
    serialized_routes = [route.serialize() for route in routes]
    user = request.user
    return {
        'routes': serialized_routes,
        'user': user.bus.serialize() if user.bus is not None else None
    }
