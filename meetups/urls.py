from django.urls import path
from . import views


urlpatterns = [
    # domain.com/meetups
    path('meetups/', views.index, name='all-meetups'),

    # domain.com/meetups/success
    path('meetups/success', views.confirm_registration,
         name='confirm-registration'),

    # domain.com/meetups/<paramater> GET & POST one url
    path('meetups/<slug:meetup_slug>',
         views.meetup_details, name='meetup-details')
]
