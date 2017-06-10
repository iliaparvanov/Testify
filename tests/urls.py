from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(r'^solve/', views.solve, name='solve'),
    url(r'^add/', views.addTest, name='addTest'),
    url(r'^add_q/', views.addQuestions, name='add_q'),
    url(r'^add_a/', views.addAnswers, name='add_a'),
]
