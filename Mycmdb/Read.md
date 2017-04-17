## CMDB ##
author：学神IT-Python-VIP-1611班-狗哥

安装准备：

	客户端操作系统：Centos 7.2
	Python版本：2.7.12
	Django版本：1.8.2

安装第三方模块：

	django==1.8.2
	paramiko
	MySQL-python

客户端采集数据发送的脚本是getmessage.py文件，通过在客户端运行这个文件就可以不断地向系统发送数据并且更新系统数据库数据。

## 目前已经实现的功能 ##

CMDB资产管理：
用户登录:
	用户登录
	用户注册
	用户修改密码
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/login.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/login.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/register.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/register.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/password.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/password.png)
资产管理:

	 资产列表
	 资产添加
	 资产修改和删除
 
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/totlist.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/totlist.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/addlist.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/addlist.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/reviselist.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/reviselist.png)


主机管理:

	 主机列表
	 主机详情页
	 主机添加
	 主机修改和删除
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/hostlist.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/hostlist.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/hostdis.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/hostdis.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/addhost.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/addhost.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/revisehost.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/revisehost.png)


远程管理:

	 客户端列表
	 客户端动态图
	 客户端远程登录
	 客户端web shell
	
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/localhostlist.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/localhostlist.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/chart.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/chart.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/localhostlogin.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/localhostlogin.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/webshell.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/webshell.png)
	
用户管理:

	 用户列表
	 用户添加
	 角色列表
	 角色成员管理
	 修改角色
	
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/userlist.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/userlist.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/adduser.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/adduser.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/rolelist.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/rolelist.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/member.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/member.png)
[https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/reviserole.png](https://github.com/crx666/cmdb/blob/master/Mycmdb/static/image/reviserole.png)

	