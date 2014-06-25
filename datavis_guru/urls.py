from django.conf.urls import patterns, include, url
from main_app import views
from main_app.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datavis_guru.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^home/$', home),
    url(r'^$', index),
    url(r'^(?P<page_name>[\w]+).html$', views.default, name='default'),
)
