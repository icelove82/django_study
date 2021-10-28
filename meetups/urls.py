from django.urls import path
from . import views


urlpatterns = [
    # domain.com/meetups
    path('meetups/', views.index, name='all-meetups'),

    # domain.com/meetups/<paramater>
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup_details')
]
