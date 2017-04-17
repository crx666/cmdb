#coding:utf-8
from django.db import models
from User.models import *

class BaseModel(models.Model):
    delete_flag = models.CharField(max_length = 4,verbose_name = "删除标志")

class Server(BaseModel):
    hostname = models.CharField(max_length=32, verbose_name="主机名")
    ip = models.CharField(max_length=32, verbose_name="ip")
    Mac = models.CharField(max_length=32, verbose_name="物理地址")
    cpu = models.CharField(max_length=32, verbose_name="cpu")
    Mem = models.CharField(max_length=32, verbose_name="内存")
    Disk = models.CharField(max_length=32, verbose_name="磁盘")
    system = models.CharField(max_length=32, verbose_name="系统")
    IO = models.CharField(max_length=32, verbose_name="IO")
    lastLogin = models.DateTimeField(verbose_name="上次登录时间")
    lastLoginUser = models.IntegerField(verbose_name="上次登录用户")
    isActive = models.CharField(max_length=32, verbose_name="是否被激活")

class Asset(BaseModel):
    number = models.CharField(max_length=32, verbose_name="资产号")
    name = models.CharField(max_length=32, verbose_name="资产名称")
    type = models.CharField(max_length=32, verbose_name="资产类型")
    ip = models.CharField(max_length=32, verbose_name="资产ip")
    service = models.CharField(max_length=32, verbose_name="业务方向")
    statue = models.BooleanField(default=True, verbose_name='资产状态')

class Asset_user(BaseModel):
    asset_id = models.CharField(max_length=32, verbose_name="资产id")
    user_id = models.CharField(max_length=32, verbose_name="用户id")
# Create your models here.
