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
        form = forms.RegistrationForm(request.POST)
        if forms.is_valid():
            user = User.objects.create_user(
                                            username = form.cleaned_data['username'],
                                            email = form.cleaned_data['email'], 
                                            password1 = form.cleaned_data['password1'], 
                                            password2 = form.cleaned_data['password2'],
                                            )
            return HttpResponseRedirect('/daftar/selesai/')
        else:
            form = RegistrationForm()
            variables = RequestContext(request, {'form': form })
 
    return render_to_response('templates/daftar.html',variables,)
 
def register_success(request):
        return render_to_response('templates/selesai.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response('home.html', { 'user': request.user })
            