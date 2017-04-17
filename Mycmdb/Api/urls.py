from django.conf.urls import include, url


urlpatterns = [
    url(r'hostlist$', "Api.views.hostlist"),
    url(r'photo/(\d{1,2})', "Api.views.photo"),
    url(r'login/(\d{1,2})', "Api.views.login"),
    url(r'webshell','Api.views.webshell'),
    url(r'connecthost', 'Api.views.connecthost'),
    url(r'logout', 'Api.views.logout'),
    url(r'command', 'Api.views.command'),
    url(r'message', 'Api.views.message'),
    url(r'Get', 'Api.views.Get'),
    url(r'revise/(\d{1,2})', 'Api.views.revise'),
    url(r'delete/(\d{1,2})', 'Api.views.delete'),

]