from django.http import HttpResponse
import datetime

def about(request):
    html = "<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>DAMS &#8250</title>
    </head><body>
    <h1>First Things First</h1>
    <p>Welcome. WordPress is a very special project to me. Every developer and contributor adds something unique to the mix, and together we create something beautiful that I'm proud to be a part of. Thousands of hours have gone into WordPress, and we're dedicated to making it better every day. Thank you for making it part of your world.</p>
    <p style="text-align: right">&#8212</p>"
    return HttpResponse(html)

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>Waktu sekarang %s. </body></html>" % now
    return HttpResponse(html)
