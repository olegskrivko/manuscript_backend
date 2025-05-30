from django.contrib import admin
from .models import Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'journal', 'author', 'phase', 'status', 'submission_date','is_overdue', 'is_archived')
    list_filter = ('phase', 'status', 'is_overdue', 'is_archived')
    search_fields = ('title', 'author__username', 'journal__journal_title')

    readonly_fields = ('last_action_date',)  # to see it in admin view
