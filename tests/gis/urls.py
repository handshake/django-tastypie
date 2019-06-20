from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^api/', include('gis.api.urls')),
)
