from .models import Route


def serialize_state(request, user=None):
    routes = Route.objects.all()
    serialized_routes = [route.serialize() for route in routes]
    if user is None:
        user = request.user
    return {
        'routes': serialized_routes,
        'user': user.bus.serialize() if user.bus is not None else None
    }
