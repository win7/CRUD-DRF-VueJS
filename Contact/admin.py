from django.contrib import admin
from .models import Friend
# Register your models here.

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    """docstring for FriendAdmin"""
    list_display = ("first_name", "last_name", "phone", "address", "birthday")