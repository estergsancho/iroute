from django.contrib import admin
from .models import Cliente, User, Vechicle, Driver, Stop,Route

admin.site.register(Cliente)
admin.site.register(User)
admin.site.register(Vechicle)
admin.site.register(Driver)
admin.site.register(Route)
admin.site.register(Stop)