from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^api/', include('content_gfk.api.urls')),
)
