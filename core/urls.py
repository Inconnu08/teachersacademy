from django.conf.urls import url

from core.serializers import Logout
from core.views import UsersList, UserDetails, Registration, Login, UserProfile

users_urlpatterns = [
    url(r'^$', UsersList.as_view(), name='list-users'),
    url(r'^(?P<id>[\d]+)/$', UserDetails.as_view(), name='details'),
    url(r'^register/$', Registration.as_view(), name='registration'),
]

auth_urlpatterns = [
    url(r'^register$', Registration.as_view(), name='register'),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', Logout.as_view(), name="logout"),
]

user_profile_urlpatterns = [
    url(r'^profile/$', UserProfile.as_view(), name='me-details'),
]
