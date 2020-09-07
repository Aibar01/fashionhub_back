from django.contrib import admin
from .models import Email


class EmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'creation_time']
    list_display_links = ['id', 'email']
    search_fields = ['email']


admin.site.register(Email, EmailAdmin)