from django.conf.urls import patterns, include, url
from idb import views
from django.contrib import admin
from django.conf.urls import patterns
from django.conf import settings
from django.conf.urls.static import static

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
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
