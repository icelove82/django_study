from django.urls import path
from . import views


urlpatterns = [
    # domain.com/meetups
    path('meetups/', views.index),

    # domain.com/meetups/<paramater>
    path('meetups/<slug:meetup_slug>', views.meetup_details)
]
