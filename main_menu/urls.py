from django.conf.urls import url
from . import views

app_name = 'main_menu'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]