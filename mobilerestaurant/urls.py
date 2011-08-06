from django.conf.urls.defaults import *
from django.contrib import admin


urlpatterns = patterns('',
	url(r'^$', 'mobilerestaurant.views.welcome'),
	url(r'^order$', 'mobilerestaurant.views.place_order'),
	url(r'^bill$', 'mobilerestaurant.views.bill'),
	url(r'^placed$', 'mobilerestaurant.views.placed'),
)
