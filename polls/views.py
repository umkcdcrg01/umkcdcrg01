from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll
# Create your views here.

def index(request):
	lastest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	output = "------".join([p.question for p in lastest_poll_list ])
	return HttpResponse(output)

def detail(request, poll_id):
	return HttpResponse("You are looking at poll %s" % poll_id)
 
def results(request, poll_id):
	return HttpResponse("you are looking at the results of poll %s" % poll_id)

def vote(request, poll_id):
	return HttpResponse("You are voting for poll %s" % poll_id)