from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^login$', views.index), 
  		    						
  ]