from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^task/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
