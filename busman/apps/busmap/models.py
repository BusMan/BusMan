from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# Create your models here.
class Route(models.Model):
    """A bus route (e.g. TJ-24)"""

    ARRIVAL_STATUSES = (('a', 'Arrived (In the lot)'), ('d', 'Delayed'), ('o', 'On Time (Expected)'))

    route_name = models.CharField(max_length=30, unique=True)
    space = models.CharField(max_length=4, blank=True)
    bus_number = models.CharField(max_length=5, blank=True)
    status = models.CharField('arrival status', choices=ARRIVAL_STATUSES, max_length=1, default='o')

    def reset_status(self):
        """Reset status to (on time) """
        self.status = 'o'
        self.space = ''
        self.save()

    def serialize(self):
        return {
            'id': self.id,
            'routeName': self.route_name,
            'space': self.space,
            'status': self.status
        }


class UserBusInfo(models.Model):
    user = models.OneToOneField(User, related_name="bus", on_delete=models.CASCADE)
    route = models.ForeignKey(Route, null=True, blank=True, on_delete=models.SET_NULL)
    is_bus_admin = models.BooleanField(default=False)

    @property
    def is_admin(self):
        """Returns whether user can assign buses
        """
        return self.is_bus_admin or self.user.is_superuser

    def serialize(self):
        name = self.user.first_name
        if name is None or len(name) == 0:
            name = self.user.username
        return {
            'route_id': self.route.id if self.route is not None else None,
            'is_admin': self.is_admin,
            'name': name
        }


def attach_bus_info(instance, created, raw, **kwargs):
    if not created or raw:
        return
    route_info, _ = UserBusInfo.objects.get_or_create(user=instance)
    route_info.save()


post_save.connect(attach_bus_info, sender=User, dispatch_uid="attach_bus_info")

