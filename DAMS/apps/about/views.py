from django.http import HttpResponse
import datetime

def about(request):
    html = ""
    return HttpResponse(html)

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>Waktu sekarang %s. </body></html>" % now
    return HttpResponse(html)

