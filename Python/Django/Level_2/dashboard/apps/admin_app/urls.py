from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^create_user$', views.create_user, name="create_user"),
	url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
]