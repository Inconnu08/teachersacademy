from django.conf.urls import url
from task.views import TaskList


task_urlpatterns = [
    url(r'^$', TaskList.as_view(), name='list'),
]