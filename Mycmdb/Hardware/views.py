from django.shortcuts import render_to_response
from User.views import *
from models import *
import datetime
from django.http import HttpResponseRedirect,JsonResponse


@login_valid
def list(request):
    username = request.session["username"]
    server = Server.objects.all()
    return render_to_response('Hardwaretemplate/hdlist.html',locals())

@login_valid
def totlelist(request):
    username = request.session["username"]
    asset = Asset.objects.all()
    return render_to_response('Hardwaretemplate/totlelist.html',locals())

def assets(request):
    username = request.session["username"]
    if request.method=='POST' and request.POST:
        a = Asset()
        statue = request.POST['statue']
        if statue =='1':
            statue = True
        else:
            statue = False
        a.number = request.POST['number']
        a.name = request.POST['name']
        a.type = request.POST['type']
        a.ip = request.POST['ip']
        a.statue = statue
        a.service = request.POST['service']
        a.save()
        return HttpResponseRedirect('/Hardware/totlelist')
    else:
        return render_to_response('Hardwaretemplate/asset.html', locals())

@login_valid
def addhost(request):
    username = request.session["username"]
    if request.method =='POST' and request.POST:
        s = Server()
        s.hostname = request.POST['hostname']
        s.ip = request.POST['ip']
        s.Mac = request.POST['mac']
        s.cpu = request.POST['cpu']
        s.Mem = request.POST['mem']
        s.Disk = request.POST['disk']
        s.system = request.POST['system']
        s.IO = request.POST['io']
        s.lastLogin = datetime.datetime.now()
        s.lastLoginUser = request.POST['last_user']
        s.isActive = request.POST['active']
        s.delete_flag = 'N'
        s.save()
        return HttpResponseRedirect('/Hardware/list')
    else:
        return render_to_response('Hardwaretemplate/addhost.html',locals())


def discri(request,sid):
    username = request.session["username"]
    id = int(sid)
    obj = Server.objects.get(id = id)
    return render_to_response('Hardwaretemplate/discri.html',locals())

def delhost(request):
    statue = {'valid':'success'}
    if request.method=='POST' and request.POST:
        id = int(request.POST['id'])
        s = Server.objects.get(id = id)
        s.delete()
        return JsonResponse(statue)
    else:
        statue['valid']='false'
        return JsonResponse(statue)


def rehost(request,sid):
    username = request.session["username"]
    id = int(sid)
    obj = Server.objects.get(id=id)
    return render_to_response('Hardwaretemplate/rehost.html',locals())


def revise(request):
    if request.method == 'POST' and request.POST:
        statue = {'valid': 'success'}
        id = request.POST['id']
        s = Server.objects.get(id = id)
        s.hostname = request.POST['hostname']
        s.ip = request.POST['ip']
        s.Mac = request.POST['mac']
        s.cpu = request.POST['cpu']
        s.Mem = request.POST['mem']
        s.Disk = request.POST['disk']
        s.system = request.POST['system']
        s.IO = request.POST['io']
        s.lastLogin = datetime.datetime.now()
        s.lastLoginUser = request.POST['last_user']
        s.isActive = request.POST['active']
        s.save()
        return JsonResponse(statue)
    else:
        statue={'valid':'false'}
        return JsonResponse(statue)

def reasset(request,sid):
    id = int(sid)
    username = request.session["username"]
    asset = Asset.objects.get(id = id)
    return render_to_response('Hardwaretemplate/reasset.html',locals())

def reassetvalid(request,sid):
    if request.method=='POST' and request.POST:
        id = int(sid)
        asset = Asset.objects.get(id=id)
        statue = request.POST['statue']
        if statue == '1':
            statue = True
        else:
            statue = False
        asset.number = request.POST['number']
        asset.name = request.POST['name']
        asset.ip = request.POST['ip']
        asset.service = request.POST['service']
        asset.statue = statue
        asset.type = request.POST['type']
        asset.save()
        return HttpResponseRedirect('/Hardware/totlelist')
    else:
        return render_to_response('Hardwaretemplate/reasset.html')

def delete(request,sid):
    id = int(sid)
    asset = Asset.objects.get(id=id)
    asset.delete()
    return HttpResponseRedirect('/Hardware/totlelist')


# Create your views here.
