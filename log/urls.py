from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^task/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^task/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    path('delete_all/', views.post_delete_all, name='post_delete_all'),

]
