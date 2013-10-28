from DAMS.apps.login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

@csrf_protect
def register(request):
    if request.method == 'POST':
        forms = forms.RegistrationForm(request.POST)
        if forms.is_valid():
            user = User.object