from django.contrib import admin
from .models import APIPermissionModel


@admin.register(APIPermissionModel)
class ApiPermissionAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['pattern', 'method', 'active', 'comment', 'created_at']
    list_filter = ['method', 'active']
    search_fields = ['pattern', 'comment']
