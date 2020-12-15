from django.contrib import admin
from flightApp.models import Flight , Passenger , Reservation

admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation)
