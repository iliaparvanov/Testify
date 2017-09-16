from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^password-change/$', views.password_change, name='password_change'),
    url(r'^search/$', views.search, name='search'),
    url(r'^userPage/$', views.userPage, name='userPage'),
    url(r'^sendingMessege/$', views.sendingMessege, name='sendingMessege'),
    url(r'^sendFriendRequest/$', views.sendFriendRequest, name='sendFriendRequest'),
    url(r'^messegeSend/$', views.messegeSend, name='messegeSend'),
    url(r'^profile_managment/$', views.profile_managment, name='profile_managment'),
    url(r'^password-change-done/$', views.index, name='password_change_done'),
    url(r'^inbox/$', views.inbox, name='inbox'),
    url(r'^uploadProfilePic/$', views.uploadProfilePic, name='uploadProfilePic'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^solve-choose-category/', views.solveChooseCategory, name='solveChooseCategory'),
    url(r'^solve-choose-test/$', views.solveChooseTest, name='solveChooseTest'),
    url(r'^solve-first-question/', views.solveFirstQuestion, name='solveFirstQuestion'),
    url(r'^solve-next-questions/', views.solveNextQuestions, name='solveNextQuestions'),
    url(r'^create-test/', views.createTest, name='createTest'),
    url(r'^add-first-question/', views.addFirstQuestion, name='addFirstQuestion'),
    url(r'^add-next-questions/', views.addNextQuestions, name='addNextQuestions'),
    url(r'^delete-tests/', views.deleteTests, name='deleteTests'),
    url(r'^see-first-mistake/', views.seeFirstMistake, name='seeFirstMistake'),
    url(r'^see-mistakes/', views.seeMistakes, name='seeMistakes'),
]
