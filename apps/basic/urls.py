from django.contrib import admin
from django.urls import path
from django.views.static import serve

from apps.basic import views
from myshop_back import settings

urlpatterns = [
    path('index/',views.index),
#     path('user_login/',views.user_login),
#     path('ajax_login_data/',views.ajax_login_data),
]
