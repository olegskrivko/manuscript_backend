from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Journal
from .serializers import JournalSerializer
from django.db.models.functions import Lower
from rest_framework.decorators import api_view
from rest_framework.response import Response

# List and search/filter
class JournalList(generics.ListAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ['journal_title']
    ordering_fields = ['journal_id', 'journal_title', 'issn_print', 'issn_online', 'status']
    ordering = ['journal_id']

@api_view(['GET'])
def journal_suggestions(request):
    query = request.GET.get('query', '')
    if not query:
        return Response({'results': []})

    journals = Journal.objects.filter(journal_title__icontains=query).order_by(Lower('journal_title'))[:10]
    return Response({
        'results': [{'journal_id': j.journal_id, 'journal_title': j.journal_title} for j in journals]
    })

class JournalDetail(generics.RetrieveAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class JournalCreate(generics.CreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class JournalUpdate(generics.UpdateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
