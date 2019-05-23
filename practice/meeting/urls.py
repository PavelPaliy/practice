from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index_url'),
    path('new/', views.create, name = 'create_meeting_url'),
    path('result/', views.result, name = 'result_create_url'),
    path('vote/<str:slug>/', views.voteDetail, name = 'vote_detail_url'),


]