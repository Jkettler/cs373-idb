from django.views.generic import TemplateView
from idb.models import Senator, Committee, Bill
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core import serializers
import json


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def about(request):
    template = loader.get_template('about.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def bills(request):
    latest_bills_list = Bill.objects.order_by('-date_proposed')
    template = loader.get_template('bills.html')
    context = RequestContext(request, {
        'latest_bills_list': latest_bills_list,
    })
    return HttpResponse(template.render(context))


def senators(request):
    latest_senators_list = Senator.objects.order_by('name')
    template = loader.get_template('senators.html')
    context = RequestContext(request, {
        'latest_senators_list': latest_senators_list,
    })
    return HttpResponse(template.render(context))


def committees(request):
    latest_committees_list = Committee.objects.order_by('name')
    template = loader.get_template('committees.html')
    context = RequestContext(request, {
        'latest_committees_list': latest_committees_list,
    })
    return HttpResponse(template.render(context))

def Senators_Bills(request, senator_id):
    sen_bills = Senator.objects.get(id=senator_id).bill_set.all()
    bills = serializers.serialize("json", [Bill.objects.get(id=bill.id) for bill in sen_bills])    
    return HttpResponse(bills)

def Senators_Committees(request, senator_id):
    sen_committees = Senator.objects.get(id=senator_id).committee_set.all()
    committees = serializers.serialize("json", [Committee.objects.get(id=com.id) for com in sen_committees])    
    return HttpResponse(committees)

def Bills_Authors(request, bill_id):
    bill_auths = Bill.objects.get(id=bill_id).authors.all()
    auths = serializers.serialize("json", [Senator.objects.get(id=auth.id) for auth in bill_auths])    
    return HttpResponse(auths)

def Committees_Senators(request, committee_id):
    committee_senators = Committee.objects.get(id=committee_id).senators.all()
    senators = serializers.serialize("json", [Senator.objects.get(id=sen.id) for sen in committee_senators])    
    return HttpResponse(senators)

def Committees_Bills(request, committee_id):
    committee_bills = Committee.objects.get(id=committee_id).bill_set.all()
    bills = serializers.serialize("json", [Bill.objects.get(id=bill.id) for bill in committee_bills])    
    return HttpResponse(bills)

class SenatorView(TemplateView):
    template_name = "senator.html"
    def get_context_data(self, **kwargs):
        context = super(SenatorView, self).get_context_data(**kwargs)
        senator = Senator.objects.get(id=str(self.args[0]))
        context['senator'] = senator
        context['bills'] = senator.bills.all()
        context['committees'] = senator.senator_set.all()
        return context


class BillView(TemplateView):
    template_name = "bill.html"
    def get_context_data(self, **kwargs):
        context = super(BillView, self).get_context_data(**kwargs)
        bill = Bill.objects.get(id=str(self.args[0]))
        context['bill'] = bill
        context['authors'] = bill.bill_set.all()
        context['voters'] = bill.voters.all()
        return context


class CommitteeView(TemplateView):
    template_name = "committee.html"

    def get_context_data(self, **kwargs):
        context = super(CommitteeView, self).get_context_data(**kwargs)
        committee = Committee.objects.get(id=str(self.args[0]))
        context['committee'] = committee
        context['senator_set'] = committee.senators.all()
        context['bills'] = committee.originating_committee_set.all()
        return context
