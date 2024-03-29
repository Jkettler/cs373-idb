from django.views.generic import TemplateView
from idb.models import Senator, Committee, Bill, Vote
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core import serializers
from django.db import connection
from idb.queries import *
from django.utils import six
from django.views import generic
from django.views.generic.list import BaseListView
import watson
import json


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def about(request):
    template = loader.get_template('about.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def apipage(request):
    template = loader.get_template('apipage.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))    

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def queries(request):
    cursor = connection.cursor()
    #Query 1
    cursor.execute(q1())
    q1Dict = dictfetchall(cursor)
    #Query 2
    cursor.execute(q2())
    q2Dict = dictfetchall(cursor)
    #Query 2
    cursor.execute(q3())
    q3Dict = dictfetchall(cursor)
    #Query 4
    cursor.execute(q4())
    q4Dict = dictfetchall(cursor)
    #Query 5
    cursor.execute(q5())
    q5Dict = dictfetchall(cursor)
    context = RequestContext(request, {
        'q1Text' : q1(),
        'q1Dict': q1Dict,
        'q2Text' : q2(),
        'q2Dict' : q2Dict,
        'q3Text' : q3(),
        'q3Dict': q3Dict,
        'q4Text' : q4(),
        'q4Dict' : q4Dict,
        'q5Text' : q5(),
        'q5Dict' : q5Dict,
    })
    template = loader.get_template('queries.html')
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

def Bills_Votes(request, bill_id):
    bill_votes = Bill.objects.get(id=bill_id).vote_set.all()

    retlist = []
    for vote in bill_votes:
        currdic = {}
        currdic['senator'] = vote.senator.id
        currdic['bill'] = vote.bill.id
        currdic['vote'] = vote.vote
        currdic['date_voted'] = str(vote.date_voted)
        retlist.append(currdic)


    #votes = serializers.serialize("json", [Vote.objects.get(id=vote.id).fields for vote in bill_votes])    
    return HttpResponse(json.dumps(retlist))    

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
        context['bills'] = senator.bill_set.all()
        context['chair'] = senator.committee_chair_set.all()
        context['vice_chair'] = senator.committee_vice_chair_set.all()
        context['committees'] = senator.committee_set.all()
        context['img_counter'] = enumerate(senator.pictures_set.all())
        context['img_links'] = enumerate(senator.pictures_set.all())
        # context['committees'] = senator.senator_set.all()
        return context


class BillView(TemplateView):
    template_name = "bill.html"
    def get_context_data(self, **kwargs):
        context = super(BillView, self).get_context_data(**kwargs)
        bill = Bill.objects.get(id=str(self.args[0]))
        context['bill'] = bill
        context['authors'] = bill.authors.all()
        context['voters'] = bill.voters.all()
        
        votes = bill.vote_set.all()
        context['votes'] = votes
        votes_vote = [vote.vote for vote in votes]
        if not votes_vote :
            context['votes_summary'] = "No voting record"
        else :
            counts = dict((i[0], votes_vote.count(i[0])) for i in Vote.VOTE_TYPES)
            context['votes_summary'] = "{0} Ayes, {1} Nays, {2} Present Not Voting, {3} Absent - {4}".format(counts["AYE"], counts["NAY"], counts["PNV"], counts["ABS"], votes.first().date_voted)
        return context


class CommitteeView(TemplateView):
    template_name = "committee.html"

    def get_context_data(self, **kwargs):
        context = super(CommitteeView, self).get_context_data(**kwargs)
        committee = Committee.objects.get(id=str(self.args[0]))
        context['committee'] = committee
        context['senator_set'] = committee.senators.all()
        context['bills'] = committee.bill_set.all()
        return context

# Mixin taken from watson
class SearchMixin(object):
    
    """Base mixin for search views."""
    
    context_object_name = "search_results"
    
    query_param = "q"
    
    def get_query_param(self):
        """Returns the query parameter to use in the request GET dictionary."""
        return self.query_param
    
    models = ()
    
    def get_models(self):
        """Returns the models to use in the query."""
        return self.models 
    
    exclude = ()
    
    def get_exclude(self):
        """Returns the models to exclude from the query."""
        return self.exclude
    
    def get_queryset(self):
        """Returns the initial queryset."""
        return watson.search(self.query, models=self.get_models(), exclude=self.get_exclude())
    
    def get_query(self, request):
        """Parses the query from the request."""
        return request.GET.get(self.get_query_param(), "").strip()
    
    empty_query_redirect = None
    
    def get_empty_query_redirect(self):
        """Returns the URL to redirect an empty query to, or None."""
        return self.empty_query_redirect
    
    extra_context = {}
    
    def get_extra_context(self):
        """
        Returns any extra context variables.
        
        Required for backwards compatibility with old function-based views.
        """
        return self.extra_context
    
    def get_context_data(self, **kwargs):
        """Generates context variables."""
        context = super(SearchMixin, self).get_context_data(**kwargs)
        context["query"] = self.query
        # Process extra context.
        for key, value in six.iteritems(self.get_extra_context()):
            if callable(value):
                value = value()
            context[key] = value
        return context
    
    def get(self, request):
        """Performs a GET request."""
        self.query = self.get_query(request)
        if not self.query:
            empty_query_redirect = self.get_empty_query_redirect()
            if empty_query_redirect:
                return redirect(empty_query_redirect)
        return super(SearchMixin, self).get(request)


class IdbSearchView(SearchMixin, generic.ListView):
    template_name = "search.html"

