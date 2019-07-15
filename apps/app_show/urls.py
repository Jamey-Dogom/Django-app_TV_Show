from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.add_show),
    url(r'^shows/create_show$', views.create_show),
    url(r'^shows/(?P<show_id>[0-9]+)$', views.display_show),
    url(r'^shows/(?P<show_id>[0-9]+)/edit', views.update_show),
    url(r'^shows/(?P<show_id>[0-9]+)/update', views.update),
    url(r'^shows/(?P<show_id>[0-9]+)/delete', views.delete),
]