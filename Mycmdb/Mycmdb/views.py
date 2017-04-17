from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from User.views import login_valid

@login_valid
def index(request):
    username = request.session['Data']['name']
    return render_to_response("index.html",locals())

def base(request):
    return render_to_response("base.html",locals())
