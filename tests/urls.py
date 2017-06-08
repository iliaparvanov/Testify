from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(r'^solve/', views.solve, name='solve'),
    url(r'^add/', views.add, name='add'),
]
