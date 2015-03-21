from django.conf.urls import url
from events import views


urlpatterns = [
    url(r'^events/$', views.EventList.as_view(), name="events"),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
    url(r'^events/category/(?P<category>\D+)/$',
        views.EventCategoryList.as_view()),
    url(r'^events/person/(?P<person>\D+)/$', views.EventPersonList.as_view()),
    url(r'^events/time/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
        views.EventTimeList.as_view()),
]
