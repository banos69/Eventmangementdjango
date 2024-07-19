from django.contrib import admin
from .models import *

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'event', 'ticket', 'quantity', 'payment_status')



