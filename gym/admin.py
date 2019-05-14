from django.contrib import admin

# Register your models here.
from gym.models import Gym, GymImage

admin.site.register(Gym)
admin.site.register(GymImage)