from django.shortcuts import render_to_response
from models import *
import paramiko,datetime
from django.http import JsonResponse,HttpResponseRedirect

def hostlist(request):
    username = request.session["username"]
    hd = Hdconnect.objects.all()
    return render_to_response('Apitemplate/hostlist.html',locals())

def message(request):
    resutl = {"statue": ""}
    if request.method == "POST" and request.POST:
        cpu_count = request.POST["cpu_count"]
        mem_rate = request.POST['mem_rate']
        disk_rate = request.POST['disk_rate']
        ip = request.POST['ip']
        cpu_user = request.POST['cpu_user']
        cpu_user = cpu_user.encode('utf-8')
        cpu_user = float(cpu_user)
        cpu_user = int(cpu_user)
        hd = Hdconnect.objects.get(ip = ip)
        hd.cpu = cpu_count
        hd.mem = mem_rate
        hd.disk = disk_rate
        hd.save()
        t = TestData.objects.get(id =1)
        t.times = datetime.datetime.now()
        t.datas = cpu_user
        t.save()
        resutl["statue"] = "success"
    else:
        resutl["statue"] = "error"
    return JsonResponse(resutl)

def photo(request,sid):
    username = request.session["username"]
    return render_to_response('Apitemplate/map.html',locals())

def revise(request,sid):
    username = request.session["username"]
    id= int(sid)
    hd =Hdconnect.objects.get(id =id)
    if request.method=='POST' and request.POST:
        name = request.POST['name']
        ip = request.POST['ip']
        enable = request.POST['enable']
        if enable=='1':
            enable = True
        else:
            enable = False
        hd.name = name
        hd.ip = ip
        hd.status = enable
        hd.save()
        return HttpResponseRedirect('/Api/hostlist')
    else:
        return render_to_response('Apitemplate/revise.html',locals())

def delete(request,sid):
    id = int(sid)
    hd = Hdconnect.objects.get(id = id)
    hd.delete()
    return HttpResponseRedirect('/Api/hostlist')

def Get(request):
    d = TestData.objects.get(id =1)
    result = {'data':[d.datas,d.times.strftime("%H:%M:%S")]}
    return JsonResponse(result)

def login(request,sid):
    id = int(sid)
    hd = Hdconnect.objects.get(id = id)
    username = request.session["username"]
    return render_to_response('Apitemplate/login.html',locals())

def webshell(request):
    username = request.session["username"]
    return render_to_response('Apitemplate/webshell.html',locals())

class Login:
    def __init__(self,host,username,password):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(
            hostname=host,
            username=username,
            password=password
        )
        self.channel = self.ssh.invoke_shell()
        self.channel.settimeout(2)
    def docommand(self,command):
        command = "%s\n"%command
        self.channel.send(command)
        result_list = []
        while True:
            try:
                recv = self.channel.recv(9999)
                recv = recv.strip().splitlines()
            except:
                recv = None
            if isinstance(recv,str):
                result_list.append(recv)
            elif isinstance(recv,list):
                result_list+=recv
            else:
                break
        result = "\n".join(result_list)
        return result
    def __del__(self):
        self.channel.close()
        self.ssh.close()

m = None
def connecthost(request):
    if request.method=="POST" and request.POST:
        host = request.POST["ip"]
        username = request.POST["user"]
        password = request.POST['password']
        global m
        try:
            m = Login(host,username,password)
            statue="success"
        except Exception as e:
            m = None
            statue = "error"
    else:
        statue = "not found"
    return JsonResponse({"statue":statue})

def logout(request):
    global m
    if m:
        del m
        statue = {"status": "success"}
        m = None
    else:
        statue = {"status":"error"}
    return JsonResponse(statue)

def command(request):
    if request.method == "POST" and request.POST:
        cmd = request.POST.get('cmd')
        global m
        if m:
            result = m.docommand(cmd)
        else:
            result = "error"
        return JsonResponse({"result":result})
    return JsonResponse({"name":"xx"})





# Create your views here.
