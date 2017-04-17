from django.shortcuts import render_to_response

def index(request):
    username = request.session["username"]
    return render_to_response('Hardwaretemplate/index.html',locals())

# Create your views here.
