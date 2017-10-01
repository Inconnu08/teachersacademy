from django.conf.urls import url
from django.contrib import admin

from core.views import UsersList, UserDetails, Registration, Login

users_urlpatterns = [
    url(r'^$', UsersList.as_view(), name='list-users'),
    url(r'^(?P<id>[\d]+)/$', UserDetails.as_view(), name='details'),
    url(r'^register/$', Registration.as_view(), name='registration'),
]

auth_urlpatterns = [
    url(r'^registration$', Registration.as_view(), name='registration'),
    url(r'^login/$', Login.as_view(), name="login"),
]