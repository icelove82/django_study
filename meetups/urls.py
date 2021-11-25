from django.urls import path
from . import views


urlpatterns = [
    # domain.com/meetups
    path('', views.index, name='all-meetups'),

    # domain.com/meetups/<paramater>/success
    path('<slug:meetup_slug>/success', views.confirm_registration,
         name='confirm-registration'),

    # domain.com/meetups/<paramater> GET & POST one url
    path('<slug:meetup_slug>',
         views.meetup_details, name='meetup-details')
]
