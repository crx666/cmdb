from django.conf.urls import include, url


urlpatterns = [
    url(r'login$', "User.views.login"),
    url(r'logout$','User.views.logout'),
    url(r'register$', 'User.views.register'),
    url(r'uservalid$', 'User.views.uservalid'),
    url(r'passwdvalid$', 'User.views.passwdvalid'),
    url(r'forget$', 'User.views.forget'),
    url(r'auth$', 'User.views.auth'),
    url(r'user$', 'User.views.user'),
    url(r'addrole$', 'User.views.addrole'),
    url(r'useradd$', 'User.views.useradd'),
    url(r'authorization/(\d{1,2})', 'User.views.authorization'),
    url(r'member/(\d{1,2})', 'User.views.member'),
    url(r'revise/(\d{1,2})', 'User.views.revise'),
    url(r'revisevalid/(\d{1,2})', 'User.views.revisevalid'),
    url(r'delete/(\d{1,2})', 'User.views.delete'),
]