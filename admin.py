from django.contrib import admin

from .models import DirectoryUser

class DirectoryUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'subject', 'modified')
    list_display_links = ('user', 'room', 'subject', 'modified')
    list_filter = ('user', 'subject', 'modified')
    
admin.site.register(DirectoryUser, DirectoryUserAdmin)