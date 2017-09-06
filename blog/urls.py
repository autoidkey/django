from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list), #startpage
    url(r'^memo/', views.memo, name='memo'),
    url(r'^temp/', views.temp, name='temp'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^test/',views.test,name='test'),
    url(r'^mypage/',views.mypage,name='mypage'),
    url(r'^delete/(?P<otitle>.*)',views.delete,name='delete'), #消すと削除できなくなる
]