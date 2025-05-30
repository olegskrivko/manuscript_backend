from django.urls import path
from .views import (
    UserList,
    UserDetail,
    UserUpdate,
    CurrentUserView,  # import the new view
)

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('current/', CurrentUserView.as_view(), name='current-user'),  # new endpoint
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('<int:pk>/edit/', UserUpdate.as_view(), name='user-update'),
]
