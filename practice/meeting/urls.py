from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('', views.index, name='index_url'),
    path('new/', views.create, name = 'create_meeting_url'),
    path('result/', views.result, name = 'result_create_url'),
    path('meeting/<str:slug>/', views.voteDetail, name = 'meeting_detail_url'),

    path('logout/', views.user_logout, name='logout'),


]