from django.conf.urls import url
from . import views

urlpatterns = [
    url (r'^$', views.article_list, name='article_list'),
    url (r'^article/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    url (r'^article/new/$', views.article_new, name='article_new'),
    url (r'^like/(?P<pk>\d+)/$', views.article_like, name='article_like'),
]
