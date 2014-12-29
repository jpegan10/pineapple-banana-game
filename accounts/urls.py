from django.conf.urls import patterns, url
from accounts import views


urlpatterns = patterns('',
                    url(r'^$',views.index,name='index'),
                    url(r'^availablelines/$', views.availablelines, name='availablelines'),
                    url(r'^makewager/(?P<line_slug>[\w\-]+)/$', views.makewager, name='make_wager'),
                    url(r'^register/$', views.register, name='register'),
                    url(r'^restricted/$',views.restricted, name='restricted'),
                    url(r'^wagercomplete/$',views.wagercomplete, name='wagercomplete'),
                    url(r'^myaccount/$',views.myaccount, name='myaccount'),
                    url(r'^public_accounts/(?P<pub_username>[\w\-]+)/$', views.public_accounts, name='public_accounts'),
                    )