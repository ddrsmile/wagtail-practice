from django.conf.urls import url
from . import views

app_name = 'project.apps.joeyliu'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
