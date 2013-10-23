from django.http import HttpResponse
from DAMS.apps.about import *
def index(request):
    return HttpResponse("Index Page")