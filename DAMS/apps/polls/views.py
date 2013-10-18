# Create your views here.

from django.shortcuts import render_to_response
from models import Poll
from django.http import Http404, HttpResponse
import datetime

def lastpoll(request):
    poll_list= Poll.objects.order_by('-poll_date')[:10]
    return render_to_response('lastpoll.html', {'poll_list': poll_list})
 
def goahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    date = datetime.datetime.now()+ datetime.timedelta(hours=offset)
    html = "<html><body> In %s haour(s), it will be %s. </body></html>" % (offset,date)
    return HttpResponse(html)

def index(request):
    DAMS = "Dayah Administration Management System"
    return HttpResponse("Welcome to " + DAMS)

def detail(request, poll_id):
    return HttpResponse("Looking for poll detail?" % poll_id)

def laporan(request, poll_id):
    return HttpResponse("Looking for laporan poll?" % poll_id)

def vote(request, poll_id):
    return HttpResponse("laporan hasil vote?" % poll_id)