from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^account/(?P<user_name_slug>[\w\-]+)/$', views.account_mod, name='account_mod'),
    url(r'^alldogs/', views.alldogs, name='alldogs'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^likeddogs/', views.likeddogs, name='likeddogs'),
    url(r'^matches/', views.matches, name='matches'),
    url(r'^survey1/', views.survey1, name='survey1'),
]
