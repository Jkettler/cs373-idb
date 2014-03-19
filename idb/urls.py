from django.conf.urls import patterns, include, url
from idb import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^senator/$', views.senators, name='senators'),
    url(r'^senator/(?P<sen>\w+)/', views.senator, name='senator'),
    url(r'^committee/$', views.committees, name='committees'),
    url(r'^committee/(?P<com>\w+)/', views.committee, name='committee'),
    url(r'^bill/$', views.bills, name='bills'),
    url(r'^bill/(?P<bi>\w+)/', views.bill, name='bill'),
    url(r'^admin/', include(admin.site.urls)),
)
