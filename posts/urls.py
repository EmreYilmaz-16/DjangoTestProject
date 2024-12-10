from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', post_index),
path('add/', add_post),
path('<int:post_id>/',post_detail,name='post_detail'),
path('<int:post_id>/update',upd_post,name='update_post'),
path('newpost/', add_post),
path('<int:post_id>/delete', del_post,name='delete_post'),
]

