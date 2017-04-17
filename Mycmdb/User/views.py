#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,JsonResponse
from models import *
import datetime

def login_valid(func):
    def inner(request,*args,**kwargs):
        username = request.session.get('username')
        if username:
            userData = Myuser.objects.get(name = username)
            all_dict={
                "id":userData.id,
                'name':userData.name,
                'password':userData.password,
                'email':userData.email,
                'phone':userData.phone
            }
            request.session['Data'] = all_dict
            return func(request)
        else:
            return HttpResponseRedirect('/User/login')
    return inner


def login(request):
    if request.method == 'POST' and request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Myuser.objects.get(name=username)
            if user.password == password:
                response = HttpResponseRedirect("/index")
                request.session['username']= username
                return response
            else:
                return HttpResponseRedirect('/User/login')
        except:
            return HttpResponseRedirect('/User/login')
    return render_to_response('Usertemplate/login.html',locals())

def logout(request):          #登出函数   登出时删除cookie和session信息，然后返回login页面
    try:
        del request.session['username']
        return HttpResponseRedirect('/User/login')
    except:
        return HttpResponseRedirect('/User/login')


def register(request):
    if request.method =='POST' and request.POST:
        username = request.POST['usname']
        password = request.POST['passwd']
        email = request.POST['email']
        phone = request.POST['phone']
        make_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            user = Myuser.objects.filter(name=username)
            if user:
                return HttpResponseRedirect('/User/login#signup')
            else:
                object = Myuser()
                object.name = username
                object.password = password
                object.email = email
                object.phone = phone
                object.make_time = make_time
                object.save()
                return HttpResponseRedirect('/User/login')
        except:
            return HttpResponseRedirect('/User/login#signup')
    else:
        return render_to_response('Usertemplate/login.html')

def forget(request):
    if request.method == 'POST' and request.POST:
        name = request.POST['username']
        password = request.POST['password']
        again_password = request.POST['again_password']
        if password != again_password:
            return HttpResponseRedirect('/User/forget')
        else:
            user = Myuser.objects.filter(name=name)
            if user:
                u = Myuser.objects.get(name=name)
                u.password = password
                u.save()
                return HttpResponseRedirect('/User/login')
            else:
                return HttpResponseRedirect('/User/forget')
    else:
        return render_to_response('Usertemplate/forget.html', locals())

def uservalid(request):  # 验证用户名是否重复函数，通过注册页面的ajax函数，返回用户名是否被注册过信息
    if request.method == "POST" and request.POST:
        statue = {'valid': "true"}
        try:
            username = request.POST['username']
            user = Myuser.objects.filter(name=username)
            if user:
                statue['valid'] = 'false'
        except:
            pass
        return JsonResponse(statue)
    else:
        return render_to_response('Usertemplate/login.html', locals())



def passwdvalid(request):                     #验证注册页面两次密码是否输入相同函数，通过注册页面的ajax函数，返回密码是否相同
    if request.method == "POST" and request.POST:
        statue = {"valid":'true'}
        try:
            password = request.POST['password']
            again_password = request.POST['again_password']
            if password == again_password:
                pass
            else:
                statue['valid']='false'
        except:
            pass
        return JsonResponse(statue)
    else:
        return render_to_response('Usertemplate/register.html', locals())



def user(request):
    username = request.session["username"]
    user = Myuser.objects.all()
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_to_response('Usertemplate/user.html',locals())



def auth(request):
    username = request.session["username"]
    role = Role.objects.all()
    group_user_count = {}
    for i in role:
        group_user_count[i.id] = Myuser_Role.objects.filter(role_id=i.id).count()
    # number = Myuser_Role.objects.filter(role_id=role.id)
    return render_to_response('Usertemplate/auth.html', locals())

def useradd(request):
    if request.method =='POST' and request.POST:
        username = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        make_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            user = Myuser.objects.filter(name=username)
            if user:
                return HttpResponseRedirect('/User/useradd')
            else:
                object = Myuser()
                object.name = username
                object.password = password
                object.email = email
                object.phone = phone
                object.make_time = make_time
                object.save()
                return HttpResponseRedirect('/User/user')
        except:
            return HttpResponseRedirect('/User/useradd')
    else:
        return render_to_response('Usertemplate/useradd.html')

def addrole(request):
    username = request.session["username"]
    if request.method=='POST' and request.POST:
        name = request.POST['name']
        dis = request.POST['dis']
        action = request.POST['action']
        if action =='1':
            action = True
        else:
            action = False
        role = Role()
        role.role_name = name
        role.role_dis = dis
        role.enable = action
        role.save()
        return HttpResponseRedirect('/User/auth')
    else:
        return render_to_response('Usertemplate/addrole.html',locals())


def authorization(request,sid):
    username = request.session['username']
    id = int(sid)
    role = Role.objects.get(id=id)
    authall = Auth._meta.get_all_field_names()
    authall.remove('id')
    all_auth = Auth_Role.objects.filter(role_id=id)
    role_auth = []
    for auth in all_auth:
        auth_obj = Auth.objects.get(id = auth.auth_id)
        role_auth.append(auth_obj)
    return render_to_response('Usertemplate/authorization.html',locals())

def member(request,sid):
    username = request.session['username']
    id = int(sid)
    role = Role.objects.get(id = id )
    userall = Myuser.objects.all()
    all_user = Myuser_Role.objects.filter(role_id = id)
    role_user = []
    for user in all_user:
        user_obj = Myuser.objects.get(id=user.user_id)
        role_user.append(user_obj)
    if request.method == 'POST' and request.POST:
        # 添加用户权限
        if "groups_selected" in request.POST:
            groups_selected_List = request.POST.get("groups_selected")
            for uid in groups_selected_List:
                try:
                    user_Obj = Myuser.objects.get(id=uid)
                    Myuser_Role.objects.create(user_id = user_Obj.id,role_id=role.id)
                except Exception, e:
                    print e
        # 删除用户权限
        if "groups" in request.POST:
            groups_List = request.POST.get("groups")
            for u_id in groups_List:
                try:
                    Myuser_Role.objects.get(user_id = u_id).delete()
                except Exception, e:
                    print e
        return HttpResponseRedirect('/User/auth')
    else:
        return render_to_response('Usertemplate/member.html',locals())

def delete(request,sid):
    id = int(sid)
    role = Role.objects.get(id = id)
    role.delete()
    return HttpResponseRedirect('/User/auth')

def revise(request,sid):
    username = request.session['username']
    id = int(sid)
    role = Role.objects.get(id = id)
    return render_to_response('Usertemplate/revise.html',locals())

def revisevalid(request,sid):
    if request.method =='POST' and request.POST:
        id = int(sid)
        name = request.POST['name']
        dis = request.POST['dis']
        enable = request.POST['enable']
        if enable =='1':
            enable = True
        else:
            enable = False
        role = Role.objects.get(id=id)
        role.role_name = name
        role.role_dis = dis
        role.enable = enable
        role.save()
        return  HttpResponseRedirect('/User/auth')
    else:
        return render_to_response('Usertemplate/revise.html',locals())


# Create your views here.
