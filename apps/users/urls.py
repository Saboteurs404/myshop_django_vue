from django.contrib import admin
from django.urls import path
from django.views.static import serve

from apps.users import views
from myshop_back import settings

urlpatterns = [
    path('user_reg/',views.user_reg),
    path('user_login/',views.user_login),
    path('ajax_login_data/',views.ajax_login_data),
]
