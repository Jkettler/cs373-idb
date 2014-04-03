from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from idb.models import Senator, Bill, Committee


class SenatorResource(ModelResource):
    class Meta:
        queryset = Senator.objects.all()
        resource_name = 'senators'
        authorization = Authorization()

class BillResource(ModelResource):
    class Meta:
        senators = fields.
        resource_name = 'bills'
        queryset = Bill.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post','put','delete']


class CommitteeResource(ModelResource):
    class Meta:
        resource_name = 'committees'
        queryset = Committee.objects.all()
        allowed_methods = ['get']