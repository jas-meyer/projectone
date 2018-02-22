from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^users$', views.index, name = "my_index"),
    url(r'^users/new$', views.new, name='my_new'),
    url(r'^users/create$', views.create, name = "my_create"),
    url(r'^users/(?P<id>\d+)/edit$', views.edit, name='my_edit'),
    url(r'^users/(?P<id>\d+)/delete$', views.destroy, name='my_delete'),
    url(r'^users/(?P<id>\d+)$', views.show, name='my_show'), 
	
]