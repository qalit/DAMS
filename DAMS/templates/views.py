from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> Its is Now %s.</body></html>" % now
    return HttpResponse(html) 