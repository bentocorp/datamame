from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^index', views.index),
    url(r'^upload', views.upload),
    url(r'^heatMapGPS', views.heatMapGPS),
]
