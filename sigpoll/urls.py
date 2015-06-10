from django.conf.urls import include, url
from django.contrib import admin
import sigpoll.views

urlpatterns = [
    url(r'^$', sigpoll.views.home, name='home'),

    url(r'^aircraft/$', sigpoll.views.aircraft_visible, name='aircraft_visible'),
    url(r'^aircraft/(?P<transponder>.*)/path$', sigpoll.views.aircraft_path, name='aircraft_path'),
    url(r'^aircraft/(?P<transponder>.*)/location$', sigpoll.views.aircraft_location, name='aircraft_location'),
]
