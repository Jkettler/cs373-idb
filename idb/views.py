from django.forms import model_to_dict
from django.views.generic import TemplateView
from django.shortcuts import render
from idb.models import Senator, Committee, Bill
from django.http import HttpResponse
from django.template import RequestContext, loader
import json
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    return render(request, 'index.html') 

def bills(request):
    latest_bills_list = Bill.objects.order_by('-date_proposed')
    template = loader.get_template('bills.html')
    context = RequestContext(request, {
        'latest_bills_list': latest_bills_list,
    })
    return HttpResponse(template.render(context))

def senators(request):
    latest_senators_list = Senator.objects.order_by('-name')
    template = loader.get_template('senators.html')
    context = RequestContext(request, {
        'latest_senators_list': latest_senators_list,
    })
    return HttpResponse(template.render(context))

def committees(request):
    latest_committees_list = Committee.objects.order_by('-name')
    template = loader.get_template('committees.html')
    context = RequestContext(request, {
        'latest_committees_list': latest_committees_list,
    })
    return HttpResponse(template.render(context))

class SenatorView(TemplateView):
    template_name = "senator.html"
    def get_context_data(self, **kwargs):
        context = super(SenatorView, self).get_context_data(**kwargs)
        query = Senator.objects.filter(id=str(self.args[0])).values()
        context['senator_bio'] = list(query)
        return context


class BillView(TemplateView):
    template_name = "bill.html"
    def get_context_data(self, **kwargs):
        context = super(BillView, self).get_context_data(**kwargs)
        query = Bill.objects.filter(id=str(self.args[0])).values()
        context['bill_info'] = list(query)
        return context

class CommitteeView(TemplateView):
    template_name = "committee.html"
    def get_context_data(self, **kwargs):
        context = super(CommitteeView, self).get_context_data(**kwargs)
        query = Committee.objects.filter(id=str(self.args[0])).values()
        context['com_info'] = list(query)
        return context

# class SenatorList(ListView):
#     model = Senator
#
# class CommitteeList(ListView):
#     model = Committee
#
# class BillList(ListView):
#     model = Bill
