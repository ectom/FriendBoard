from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^friends$', views.friends),
    url(r'^add_friend/(?P<user_id>\d+)$', views.add_friend),
    url(r'^remove/(?P<user_id>\d+)$', views.remove),
    url(r'^user/(?P<user_id>\d+)$', views.user),
]
