"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	#url(r'^admin/', admin.site.urls),
	url(r'^', include('blog.urls')), #add
	#url(r'^', include('blog.urls')),
	#url(r'^memo/', include('blog.urls')),
	#url(r'^temp/', include('blog.urls')),
	#url(r'^post/(?P<pk>[0-9]+)/', include('blog.urls')),
	#url(r'^post/new/', include('blog.urls')),
	#url(r'^post/(?P<pk1>[0-9]+)/edit/', include('blog.urls')),
	#another apply
	url(r'^guestboard/', include('guestboard.urls', namespace='guestboard')),  #add guestboard

]

#^ :文字列開始 $:文字列終わり
#namespaceはhtmlファイルの方で指定