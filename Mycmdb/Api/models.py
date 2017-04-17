#coding:utf-8
from django.db import models

class Hdconnect(models.Model):
    name = models.CharField("主机名",max_length=32)
    ip = models.CharField("主机地址",max_length=32)
    cpu = models.CharField('cpu使用率',max_length=32)
    mem = models.CharField('内存使用率',max_length=32)
    disk = models.CharField('磁盘使用率',max_length=32)
    status = models.BooleanField("主机状态",default=False)
    password = models.CharField('密码',max_length=32)
    delete_flag = models.CharField(max_length=4)

class TestData(models.Model):
    times = models.DateTimeField(auto_now = True)
    datas = models.IntegerField()


# Create your models here.
