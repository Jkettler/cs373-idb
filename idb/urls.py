from django.conf.urls import patterns, include, url
from idb import views
from django.contrib import admin
from django.conf.urls import patterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^senators/(\d+)/$', views.SenatorView.as_view()),
    url(r'^senators/$', views.senators, name="senators"),
    url(r'^committees/(\d+)/$', views.CommitteeView.as_view()),
    url(r'^committees/$', views.committees, name="committees"),
    url(r'^bills/(\d+)/$', views.BillView.as_view()),
    url(r'^bills/$', views.bills, name="bills"),
)
