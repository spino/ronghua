from django.conf.urls import url
#from django.urls import path

from . import views

app_name = 'schedule'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /schedule/5/
    url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail'),
    
    url(r'^(?P<b_id>[0-9]+)/bybranch/$', views.bybranch, name='bybranch'),
    
    url(r'^(?P<pk>[0-9]+)/arrange_update/$', views.ScheduleUpdate.as_view(), name='arrange_update'),

]



