from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)
    first_name = serializers.CharField(source='author.first_name', read_only=True)  # <-- Add this line
    last_name = serializers.CharField(source='author.last_name', read_only=True)
    journal_title = serializers.CharField(source='journal.journal_title', read_only=True)
    

    class Meta:
        model = Submission
        fields = ['id', 'title', 'phase', 'status', 'submission_date', 'last_action_date',
                  'is_overdue', 'is_archived', 'author', 'journal', 'username', 'first_name', 'last_name', 'journal_title']
