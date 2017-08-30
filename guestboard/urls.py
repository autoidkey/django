from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^guestboard$', views.index, name='index'),
]