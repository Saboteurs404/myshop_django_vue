from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import *
# Register your models here.
admin.site.register(MyUser, UserAdmin)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username','email','is_active','truename','mobile']

