from django.conf.urls import patterns, include, url
from tastypie.api import Api
from alphanumeric.api.resources import ProductResource

api = Api(api_name='v1')
api.register(ProductResource(), canonical=True)

urlpatterns = api.urls
