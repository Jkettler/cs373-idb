from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from idb.models import Senator, Bill, Committee



class BillResource(ModelResource):
    authors = fields.ToManyField('idb.api.resources.SenatorResource', 'authors', full=False, null=True)
    primary_committee = fields.ToOneField('idb.api.resources.BillResource', 'primary_committee', full=False, null=True)

    class Meta:
        resource_name = 'bills'
        queryset = Bill.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post','put','delete']
        include_resource_uri = False

    def get_list(self, request, **kwargs):
            base_bundle = self.build_bundle(request=request)
            objects = self.obj_get_list(bundle=base_bundle, **self.remove_api_resource_names(kwargs))
            sorted_objects = self.apply_sorting(objects, options=request.GET)
            paginator = self._meta.paginator_class(request.GET, sorted_objects, resource_uri=self.get_resource_uri(), limit=self._meta.limit, max_limit=self._meta.max_limit, collection_name=self._meta.collection_name)
            to_be_serialized = paginator.page()
            bundles = []
            for obj in to_be_serialized[self._meta.collection_name]:
                bundle = self.build_bundle(obj=obj, request=request)
                bundles.append(self.full_dehydrate(bundle, for_list=True))
            to_be_serialized[self._meta.collection_name] = bundles
            to_be_serialized = self.alter_list_data_to_serialize(request, to_be_serialized)
            return self.create_response(request, to_be_serialized['objects'])

    def dehydrate(self, bundle):
        if (bundle.data['primary_committee']):
            arr = bundle.data['primary_committee'].split("/")
            bundle.data['primary_committee'] = int(arr[len(arr) - 2])

        i = 0
        for auth in bundle.data['authors']:
            arr = auth.split("/")
            bundle.data['authors'][i] = int(arr[len(arr) - 2])
            i += 1

        return bundle

    def hydrate(self, bundle):
        if (bundle.data['primary_committee']):
            bundle.data['primary_committee'] = "/api/committees/" + str(bundle.data['primary_committee']) + "/"

        i = 0
        for auth in bundle.data['authors']:
            bundle.data['authors'][i] = "/api/senators/" + str(bundle.data['authors'][i]) + "/"
            i += 1

        return bundle       


class CommitteeResource(ModelResource):
    bills = fields.ToManyField(BillResource, 'bill_set',  full=False, null=True)
    senators = fields.ToManyField('idb.api.resources.CommitteeResource', 'senators', full=False, null=True)
    chair = fields.ToOneField('idb.api.resources.SenatorResource', 'chair', full=False, null=True)
    vice_chair = fields.ToOneField('idb.api.resources.SenatorResource', 'vice_chair', full=False, null=True)

    class Meta:
        resource_name = 'committees'
        queryset = Committee.objects.all()
        allowed_methods = ['get','post','put','delete']
        include_resource_uri = False
        detail_uri_name = 'pk'

    def get_list(self, request, **kwargs):
        base_bundle = self.build_bundle(request=request)
        objects = self.obj_get_list(bundle=base_bundle, **self.remove_api_resource_names(kwargs))
        sorted_objects = self.apply_sorting(objects, options=request.GET)
        paginator = self._meta.paginator_class(request.GET, sorted_objects, resource_uri=self.get_resource_uri(), limit=self._meta.limit, max_limit=self._meta.max_limit, collection_name=self._meta.collection_name)
        to_be_serialized = paginator.page()
        bundles = []
        for obj in to_be_serialized[self._meta.collection_name]:
            bundle = self.build_bundle(obj=obj, request=request)
            bundles.append(self.full_dehydrate(bundle, for_list=True))
        to_be_serialized[self._meta.collection_name] = bundles
        to_be_serialized = self.alter_list_data_to_serialize(request, to_be_serialized)
        return self.create_response(request, to_be_serialized['objects'])



class SenatorResource(ModelResource):
    bills = fields.ToManyField(BillResource, 'bill_set',  full=False, null=True)
    committees = fields.ToManyField(CommitteeResource, 'committee_set', full=False, null=True)

    class Meta:
        queryset = Senator.objects.all()
        resource_name = 'senators'
        authorization = Authorization()
        allowed_methods = ['get','post','put','delete']
        include_resource_uri = False
        detail_uri_name = 'pk'

    def get_list(self, request, **kwargs):
        base_bundle = self.build_bundle(request=request)
        objects = self.obj_get_list(bundle=base_bundle, **self.remove_api_resource_names(kwargs))
        sorted_objects = self.apply_sorting(objects, options=request.GET)
        paginator = self._meta.paginator_class(request.GET, sorted_objects, resource_uri=self.get_resource_uri(), limit=self._meta.limit, max_limit=self._meta.max_limit, collection_name=self._meta.collection_name)
        to_be_serialized = paginator.page()
        bundles = []
        for obj in to_be_serialized[self._meta.collection_name]:
            bundle = self.build_bundle(obj=obj, request=request)
            bundles.append(self.full_dehydrate(bundle, for_list=True))
        to_be_serialized[self._meta.collection_name] = bundles
        to_be_serialized = self.alter_list_data_to_serialize(request, to_be_serialized)
        return self.create_response(request, to_be_serialized['objects'])
