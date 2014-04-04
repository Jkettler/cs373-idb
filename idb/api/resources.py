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
        if ('primary_committee' in bundle.data and bundle.data['primary_committee']):
            bundle.data['primary_committee'] = "/api/committees/" + str(bundle.data['primary_committee']) + "/"

        if ('authors' in bundle.data):
            i = 0
            for auth in bundle.data['authors']:
                bundle.data['authors'][i] = "/api/senators/" + str(bundle.data['authors'][i]) + "/"
                i += 1

        return bundle       


class CommitteeResource(ModelResource):
    bills = fields.ToManyField(BillResource, 'bill_set',  full=False, null=True)
    senators = fields.ToManyField('idb.api.resources.SenatorResource', 'senators', full=False, null=True)
    chair = fields.ToOneField('idb.api.resources.SenatorResource', 'chair', full=False, null=True)
    vice_chair = fields.ToOneField('idb.api.resources.SenatorResource', 'vice_chair', full=False, null=True)

    class Meta:
        resource_name = 'committees'
        queryset = Committee.objects.all()
        allowed_methods = ['get','post','put','delete']
        include_resource_uri = False
        authorization = Authorization()

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
        i = 0
        for bill in bundle.data['bills']:
            arr = bill.split("/")
            bundle.data['bills'][i] = int(arr[len(arr) - 2])
            i += 1

        i = 0
        for senator in bundle.data['senators']:
           arr = senator.split("/")
           bundle.data['senators'][i] = int(arr[len(arr) - 2])
           i += 1

        if (bundle.data['chair']):
            arr = bundle.data['chair'].split("/")
            bundle.data['chair'] = int(arr[len(arr) - 2])

        if (bundle.data['vice_chair']):
            arr = bundle.data['vice_chair'].split("/")
            bundle.data['vice_chair'] = int(arr[len(arr) - 2])

        return bundle

    def hydrate(self, bundle):
        i = 0
        if 'bills' in bundle.data:
            for bill in bundle.data['bills']:
                bundle.data['bills'][i] = "/api/bills/" + str(bundle.data['bills'][i]) + "/"
                i += 1

        if 'senators' in bundle.data:
           i = 0
           for senator in bundle.data['senators']:
               bundle.data['senators'][i] = "/api/senators/" + str(bundle.data['senators'][i]) + "/"
               i += 1

        if ('chair' in bundle.data and bundle.data['chair']):
                bundle.data['chair'] = "/api/senators/" + str(bundle.data['chair']) + "/"

        if ('vice_chair' in bundle.data and bundle.data['vice_chair']):
                bundle.data['vice_chair'] = "/api/senators/" + str(bundle.data['vice_chair']) + "/"


        return bundle      


class SenatorResource(ModelResource):
    bills = fields.ToManyField(BillResource, 'bill_set',  full=False, null=True)
    committees = fields.ToManyField(CommitteeResource, 'committee_set', full=False, null=True)

    class Meta:
        queryset = Senator.objects.all()
        resource_name = 'senators'
        allowed_methods = ['get','post','put','delete']
        include_resource_uri = False
        authorization = Authorization()

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
        i = 0
        for bill in bundle.data['bills']:
            arr = bill.split("/")
            bundle.data['bills'][i] = int(arr[len(arr) - 2])
            i += 1

        i = 0
        for senator in bundle.data['committees']:
            arr = senator.split("/")
            bundle.data['committees'][i] = int(arr[len(arr) - 2])
            i += 1

        return bundle

    def hydrate(self, bundle):
        i = 0
        if 'bills' in bundle.data:
            for bill in bundle.data['bills']:
                bundle.data['bills'][i] = "/api/bills/" + str(bundle.data['bills'][i]) + "/"
                i += 1

        if 'committees' in bundle.data:
            i = 0
            for senator in bundle.data['committees']:
                bundle.data['committees'][i] = "/api/committees/" + str(bundle.data['committees'][i]) + "/"
                i += 1

        return bundle   