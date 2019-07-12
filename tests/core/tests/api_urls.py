from django.conf.urls import include, url
from core.tests.api import Api, NoteResource, UserResource
from core.tests.resources import SubjectResource


api = Api()
api.register(NoteResource())
api.register(UserResource())
api.register(SubjectResource())

urlpatterns = [
    url(r'^api/', include(api.urls)),
]
