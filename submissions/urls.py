from django.urls import path
from .views import (
    SubmissionList,
    SubmissionCreate,
    SubmissionDetail,
    SubmissionUpdate,
    SubmissionDelete,
)

urlpatterns = [
    path('', SubmissionList.as_view(), name='submission-list'),
    path('<int:pk>/', SubmissionDetail.as_view(), name='submission-detail'),
    path('create/', SubmissionCreate.as_view(), name='submission-create'),
    path('<int:pk>/edit/', SubmissionUpdate.as_view(), name='submission-update'),
    path('<int:pk>/delete/', SubmissionDelete.as_view(), name='submission-delete'),
]
