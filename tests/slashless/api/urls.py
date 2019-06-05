from django.conf.urls import url, patterns, include
from tastypie.api import Api
from slashless.api.resources import NoteResource, UserResource

api = Api(api_name='v1')
api.register(NoteResource(), canonical=True)
api.register(UserResource(), canonical=True)

urlpatterns = patterns('',
    url(r'^api/', include(api.urls)),
)
