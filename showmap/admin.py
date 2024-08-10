# admin.py

from django.contrib import admin
from .models import UserLocation


@admin.register(UserLocation)
class UserLocationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'latitude', 'longitude', 'timestamp')
    search_fields = ('user_id', 'latitude', 'longitude')
    list_filter = ('timestamp',)
