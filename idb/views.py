from django.views.generic import TemplateView
from idb.models import Senator, Committee, Bill
from django.http import HttpResponse
from django.template import RequestContext, loader


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

class SenatorView(TemplateView):
    template_name = "senator.html"
    def get_context_data(self, **kwargs):
        context = super(SenatorView, self).get_context_data(**kwargs)
        senator = Senator.objects.get(id=str(self.args[0]))
        committees =  Committee.objects.all()
        context['senator'] = senator
        context['bills'] = senator.authored_bill_set.all()
        context['committees'] = senator.senator_set.all()
        return context


class BillView(TemplateView):
    template_name = "bill.html"
    def get_context_data(self, **kwargs):
        context = super(BillView, self).get_context_data(**kwargs)
        bill = Bill.objects.get(id=str(self.args[0]))
        context['bill'] = bill
        context['voters'] = bill.voters.all()
        return context

class CommitteeView(TemplateView):
    template_name = "committee.html"

    def get_context_data(self, **kwargs):
        context = super(CommitteeView, self).get_context_data(**kwargs)
        committee = Committee.objects.get(id=str(self.args[0]))
        context['committee'] = committee
        context['senator_set'] = committee.senators.all()
        return context
