from django.conf.urls import patterns, url
from . import test_views

urlpatterns = patterns(
    '',
    url(r'^a-url/$', test_views.a_view,
        name="a-url"),
    url(r'^a-different-url/$', test_views.a_view,
        name="a-different-url")
)
