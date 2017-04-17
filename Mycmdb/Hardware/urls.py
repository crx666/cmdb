from django.conf.urls import include, url

urlpatterns = [
    url(r'^totlelist/', "Hardware.views.totlelist"),
    url(r'^list/', "Hardware.views.list"),
    url(r'^discri/(\d{1,2})', "Hardware.views.discri"),
    url(r'^addhost/', "Hardware.views.addhost"),
    url(r'^delhost/', "Hardware.views.delhost"),
    url(r'^rehost/(\d{1,2})', "Hardware.views.rehost"),
    url(r'^revise/', "Hardware.views.revise"),
    url(r'^assets/', "Hardware.views.assets"),
    url(r'^reasset/(\d{1,2})', "Hardware.views.reasset"),
    url(r'^delete/(\d{1,2})', "Hardware.views.delete"),
    url(r'^reassetvalid/(\d{1,2})', "Hardware.views.reassetvalid"),
]