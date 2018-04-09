from django.conf.urls import url
from . import views

app_name = 'res'

urlpatterns = [
    url(r'^$', views.IndexView.as_view() , name='menu'),

    url(r'^register/$', views.UserFormView.as_view() , name='register'),

    url(r'^(?P<category_name>[a-z]+)/$', views.detail, name='detail'),
]