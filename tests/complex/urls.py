from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^api/', include('complex.api.urls')),
)
