from django.contrib.auth.models import User
from django.db import models


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


class UserBusInfo(models.Model):
    user = models.ForeignKey(User, unique=True, related_name="bus")
    route = models.ForeignKey(Route, null=True, blank=True)
    is_bus_admin = models.BooleanField(default=False)

    @property
    def is_admin(self):
        """Returns whether user can assign buses
        """
        return self.is_bus_admin or self.user.is_superuser
