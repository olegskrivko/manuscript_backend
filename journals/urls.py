from django.urls import path
from .views import (
    JournalList,
    JournalDetail,
    JournalCreate,
    JournalUpdate,
    journal_suggestions,
)

urlpatterns = [
    path('', JournalList.as_view(), name='journal-list'),
    path('search/', journal_suggestions, name='journal-suggestions'),  # autocomplete endpoint
    path('<int:pk>/', JournalDetail.as_view(), name='journal-detail'),
    path('create/', JournalCreate.as_view(), name='journal-create'),
    path('<int:pk>/edit/', JournalUpdate.as_view(), name='journal-update'),
]
