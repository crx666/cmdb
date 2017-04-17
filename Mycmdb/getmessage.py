#!usr/bin/python
#coding:utf-8

from __future__ import division
import time
import urllib
import urllib2
import psutil
import socket

def getData(url):
    while True:
        dataDict = {
                "cpu_count":psutil.cpu_count(),
		'cpu_user':psutil.cpu_times().user,
                "mem_used":psutil.virtual_memory().used/1024/1024,
                "mem_total":psutil.virtual_memory().total/1024/1024,
                "disk_used":psutil.disk_usage('/').used/1024/1024,
                'disk_total':psutil.disk_usage('/').total/1024/1024,
}

        mem_used =  dataDict['mem_used']
        mem_total =  dataDict['mem_total']
        disk_used =  dataDict['disk_used']
	disk_total =  dataDict['disk_total']
        cpu_count = dataDict['cpu_count']
	cpu_user = dataDict['cpu_user']
        a = mem_used/mem_total
        b = disk_used/disk_total
        mem_rate =  '%.2f'%a
        disk_rate = '%.2f'%b
        myname = socket.getfqdn(socket.gethostname(  ))
        ip = socket.gethostbyname(myname)
        data = {'cpu_count':cpu_count,'cpu_user':cpu_user,'mem_rate':mem_rate,'disk_rate':disk_rate,'ip':ip}

        headers = {
     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
        sendData = urllib.urlencode(data)
        req = urllib2.Request(url,data = sendData,headers = headers)
        ope = urllib2.urlopen(req)
        print ope.read()

        time.sleep(3)

if __name__ == "__main__":
   url = "http://14.20.193.17:8000/Api/message"
   while True:
        getData(url)