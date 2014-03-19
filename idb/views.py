from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html') 
def senators(request):
    return HttpResponse("this is the page of all the senators")
def senator(request, sen):
    senator = get_object_or_404(Senator, pk=sen)
    return render(request, 'senator.html', {'senator':senator})
def committees(request):
    return HttpResponse("this is the page of all committees")
def committee(request, com):
    committee = get_object_or_404(Committee, pk=com)
    return render(request, 'committee.html', {'committee':committee})
def bills(request):
    return HttpResponse("this is the page of all the bills")
def bill(request, bi):
    bill = get_object_or_404(Bill, pk=bi)
    return render(request, 'bill.html', {'bill':bill})
