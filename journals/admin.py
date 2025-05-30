from django.contrib import admin
from .models import Journal

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('journal_title', 'issn_print', 'issn_online', 'status', 'publisher', 'founder')
    search_fields = ('journal_title', 'publisher', 'founder')
    list_filter = ('status',)
