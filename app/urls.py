from django.conf.urls import url
from app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^registered/', views.registered, name='registered'),
    url(r'^signin/', views.authenticateuser, name='authenticateuser'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^survey/', views.survey, name='survey'),
    url(r'^matches/', views.matches, name = 'matches'),
    url(r'^alldogs/$', views.alldogs, name='alldogs'),
    url(r'^login/', views.authlogin, name='authlogin'),
]
