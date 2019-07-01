from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('complex.api.urls')),
]
