from django.conf.urls import patterns, url
from wagerapp import views

urlpatterns = patterns('',
                    url(r'^$', views.index, name='index'),
                    url(r'^register/$', views.register, name='register'),
                    url(r'^login/$', views.user_login, name='login'),
                    url(r'^restricted/', views.restricted, name='restricted'),
                    url(r'^logout/$', views.user_logout, name='logout'),
                    #url(r'^userprofile/$', views.userprofile,name='userprofile'),
                    url(r'^standings/$', views.standings, name='standings'),
                    url(r'^userprofile/(?P<profile_name>\w+)/$', views.userprofile, name='user_profile'),
                    )
