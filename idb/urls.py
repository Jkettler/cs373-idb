from django.conf.urls import patterns, include, url
from idb import views
from django.contrib import admin
from django.conf.urls import patterns
from django.conf import settings
from django.conf.urls.static import static
from tastypie.api import Api
from idb.api.resources import SenatorResource, BillResource, CommitteeResource

idb_api = Api(api_name='api')

idb_api.register(SenatorResource())
idb_api.register(BillResource())
idb_api.register(CommitteeResource())

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
    url(r'^about/$', views.about, name="about"),
    url(r'^api/senators/(?P<senator_id>\d+)/bills/$', views.Senators_Bills),
    url(r'^api/senators/(?P<senator_id>\d+)/committees/$', views.Senators_Committees),
    url(r'^api/bills/(?P<bill_id>\d+)/authors/$', views.Bills_Authors),
    url(r'^api/bills/(?P<bill_id>\d+)/votes/$', views.Bills_Votes),
    url(r'^api/committees/(?P<committee_id>\d+)/senators/$', views.Committees_Senators),
    url(r'^api/committees/(?P<committee_id>\d+)/bills/$', views.Committees_Bills),
	url(r'^', include(idb_api.urls)),
    url(r'^queries/$', views.queries, name="queries"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
