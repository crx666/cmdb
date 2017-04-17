#coding:utf-8
from django.db import models


class Myuser(models.Model):         #设置数据库信息
    name = models.CharField('用户名',max_length=32)
    password = models.CharField('用户密码',max_length=32)
    email = models.CharField('email',max_length=32)
    phone = models.CharField('电话',max_length=32)
    make_time = models.DateTimeField('创建时间',default='2017-03-15 20:30:20')
    delete_flag = models.CharField(max_length=4, verbose_name="删除标志",default='Y')

class Role(models.Model):
    role_name = models.CharField('角色名',max_length=32)
    role_dis = models.TextField('角色描述')
    enable = models.BooleanField(default=True, verbose_name=u'是否启用')

class Myuser_Role(models.Model):
    user_id = models.CharField('用户id',max_length=32)
    role_id = models.CharField('角色id',max_length=32)



class Auth(models.Model):
    select_host = models.BooleanField(default=False, verbose_name=u"查看资产")
    edit_host = models.BooleanField(default=False, verbose_name=u"修改资产")
    add_host = models.BooleanField(default=False, verbose_name=u"添加主机")
    delete_host = models.BooleanField(default=False, verbose_name=u"删除资产")

    add_user = models.BooleanField(default=False, verbose_name=u'添加用户')
    edit_user = models.BooleanField(default=False, verbose_name=u'修改用户')
    edit_pass = models.BooleanField(default=False, verbose_name=u"修改密码")
    delete_user = models.BooleanField(default=False, verbose_name=u"删除用户")

class Auth_Role(models.Model):
    auth_id = models.CharField('权限id', max_length=32)
    role_id = models.CharField('角色id', max_length=32)

# Create your models here.
