# submissions/filters.py
from django_filters import rest_framework as filters
from .models import Submission

class SubmissionFilter(filters.FilterSet):
    journal_title = filters.CharFilter(field_name='journal__journal_title', lookup_expr='icontains')
    submission_date = filters.DateFromToRangeFilter()
    last_action_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Submission
        fields = ['journal_title', 'phase', 'status', 'is_overdue', 'is_archived']
