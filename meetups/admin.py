from django.contrib import admin
from django.db import models
from .models import Meetup, Location, Participant

# Register your models here.


class MeetupAdminCustom(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Meetup, MeetupAdminCustom)
admin.site.register(Location)
admin.site.register(Participant)
