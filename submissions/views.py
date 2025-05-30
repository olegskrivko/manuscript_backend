from django.db.models import Case, When, Value, IntegerField
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Submission
from .serializers import SubmissionSerializer
from .filters import SubmissionFilter


class SubmissionList(generics.ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = SubmissionFilter

    search_fields = [
        'title', 'author__first_name', 'author__last_name',
        'co_authors__first_name', 'co_authors__last_name'
    ]
    ordering_fields = [
        'id', 'title', 'submission_date', 'last_action_date',
        'phase', 'status', 'journal__journal_title', 'is_overdue'
    ]

    def get_queryset(self):
            qs = super().get_queryset()
            ordering = self.request.query_params.get('ordering')

            if ordering:
                ordering_fields = [field.strip() for field in ordering.split(',')]
                return qs.order_by(*ordering_fields)

            # Default sort priority:
            # 1. Overdue → last_action_date ASC
            # 2. Phase = 'new' (not overdue) → last_action_date ASC
            # 3. Others → last_action_date ASC
            return qs.annotate(
                sort_priority=Case(
                    When(is_overdue=True, then=Value(0)),                    # Top group: overdue
                    When(phase='new', is_overdue=False, then=Value(1)),     # Next: new (not overdue)
                    default=Value(2),                                        # Last: everything else
                    output_field=IntegerField()
                )
            ).order_by('sort_priority', 'last_action_date')

# Retrieve
class SubmissionDetail(generics.RetrieveAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

# Update
class SubmissionUpdate(generics.UpdateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

# Delete
class SubmissionDelete(generics.DestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

# Create
class SubmissionCreate(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

