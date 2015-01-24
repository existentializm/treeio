# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of Treeio.
# License www.tree.io/license

<<<<<<< HEAD:core/api/urls.py
from django.conf.urls import patterns, include
=======
#from piston.resource import Resource
from django.conf.urls import *
>>>>>>> 7eb75ad5a5164e5b47a5bca3851a1b508a1ecf26:treeio/core/api/urls.py

urlpatterns = patterns('',
    (r'^auth/', include('treeio.core.api.auth.urls')),
    (r'^news/', include('treeio.news.api.urls')),
    (r'^core/', include('treeio.core.administration.api.urls')),
    (r'^projects/', include('treeio.projects.api.urls')),
    (r'^services/', include('treeio.services.api.urls')),
    (r'^sales/', include('treeio.sales.api.urls')),
    (r'^finance/', include('treeio.finance.api.urls')),
    (r'^knowledge/', include('treeio.knowledge.api.urls')),
    (r'^messaging/', include('treeio.messaging.api.urls')),
    (r'^infrastructure/', include('treeio.infrastructure.api.urls')),
    (r'^calendar/', include('treeio.events.api.urls')),
    (r'^documents/', include('treeio.documents.api.urls')),
    (r'^identities/', include('treeio.identities.api.urls')),
)