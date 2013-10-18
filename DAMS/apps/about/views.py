from django.http import HttpResponse
import datetime

def about(request):
    return HttpResponse("Dayah Administration Management System")

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>Waktu sekarang %s. </body></html>" % now
    return HttpResponse(html)
