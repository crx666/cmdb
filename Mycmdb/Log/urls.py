from django.conf.urls import include, url


urlpatterns = [
    url(r'index$', "Log.views.index")
]