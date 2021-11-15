from django.contrib import admin
from django.db import models
from .models import Meetup, Location

# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('location', )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
