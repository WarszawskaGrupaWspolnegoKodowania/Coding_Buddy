# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [

    url(
        regex=r'^$',
        view=views.ProjectListView.as_view(),
        name='list'
    ),

    url(
        regex=r'^new/$',
        view=views.ProjectCreateView.as_view(),
        name='create'
    ),

    url(
	regex=r'^(?P<slug>[-\w]+)/$',
        view=views.ProjectDetailView.as_view(),
        name='detail'
    ),

    url(
        regex=r'^(?P<slug>[-\w]+)/update/$',
        view=views.ProjectUpdateView.as_view(),
        name='update'
    ),

    url(
        regex=r'^(?P<slug>[-\w]+)/delete/$',
        view=views.ProjectDeleteView.as_view(),
        name='delete'
    ),
]
