from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^create/', views.create, name='create'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^solve/', views.solve, name='solve'),
    url(r'^add/', views.addTest, name='addTest'),
    url(r'^add_q/', views.addQuestions, name='add_q'),
    url(r'^getTest/', views.getTest, name='getTest'),
    url(r'^solveTest/', views.solveTest, name='solveTest'),
	url(r'^testChooseMath/$', views.testChooseMath, name='testChooseMath'),
    url(r'^testChooseEnglish/$', views.testChooseEnglish, name='testChooseEnglish'),
    url(r'^testChooseGeography/$', views.testChooseGeography, name='testChooseGeography'),
    url(r'^testChooseHistory/$', views.testChooseHistory, name='testChooseHistory'),
    url(r'^testChooseBiology/$', views.testChooseBiology, name='testChooseBilogy'),

]
