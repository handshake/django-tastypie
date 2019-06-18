from django.conf.urls import patterns, include, url
from tastypie.api import Api
from gis.api.resources import GeoNoteResource, UserResource

api = Api(api_name='v1')
api.register(GeoNoteResource())
api.register(UserResource())

urlpatterns = api.urls
