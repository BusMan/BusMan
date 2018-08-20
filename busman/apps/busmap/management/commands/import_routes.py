from django.core.management.base import BaseCommand
from ...models import Route


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)
        parser.add_argument('--nuke', action='store_true')
        parser.add_argument('--remove', action='store_true')

    def add_route(self, route_name):
        route, created = Route.objects.get_or_create(route_name=route_name)
        if created:
            self.stdout.write("{} was newly created.".format(route))
        else:
            self.stdout.write("{} already exists. Skipping...".format(route))

    def delete_route(self, route_name):
        try:
            route = Route.objects.get(route_name=route_name)
            route.delete()
            self.stdout.write("{} was successfully deleted.".format(route_name))
        except Route.DoesNotExist:
            self.stdout.write("{} does not exist. Skipping...".format(route_name))

    def handle(self, *args, **options):
        if options['nuke']:
            Route.objects.all().delete()
        with open(options['file'], "r") as f:
            for route_name in f:
                if options['remove']:
                    self.delete_route(route_name)
                else:
                    self.add_route(route_name)
