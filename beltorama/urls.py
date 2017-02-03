from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('apps.registration.urls', namespace='loginreg')),
    url(r'^travels/', include('apps.belt_main.urls', namespace='travels')),

]
