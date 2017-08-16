from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^solve-choose-category/', views.solveChooseCategory, name='solveChooseCategory'),
    url(r'^solve-choose-test/$', views.solveChooseTest, name='solveChooseTest'),
    url(r'^solve-first-question/', views.solveFirstQuestion, name='solveFirstQuestion'),
    url(r'^solve-next-questions/', views.solveNextQuestions, name='solveNextQuestions'),
    url(r'^create-test/', views.createTest, name='createTest'),
    url(r'^add-first-question/', views.addFirstQuestion, name='addFirstQuestion'),
    url(r'^add-next-questions/', views.addNextQuestions, name='addNextQuestions'),
    url(r'^delete-tests/', views.deleteTests, name='deleteTests'),
]
