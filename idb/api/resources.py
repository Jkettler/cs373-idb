from tastypie.resources import ModelResource
from idb.models import Senator, 


class SenatorResource(ModelResource):
    class Meta:
        queryset = Senator.objects.all()
        allowed_methods = ['get']

