__author__ = 'Pavan Kotehal'

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.student_list, name='student_list'),
    url(r'^students/$', views.list_student),
    url(r'^students/(?P<pk>[0-9]+)/$', views.student_detail),
]