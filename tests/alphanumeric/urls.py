from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^api/', include('alphanumeric.api.urls')),
)
