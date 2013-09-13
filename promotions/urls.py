from django.conf.urls import patterns, include, url

from promotions import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<promo_id>\d+)/$', views.detail, name='detail'),
)
