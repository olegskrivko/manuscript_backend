from django.urls import path
from .views import RegisterView, LoginView, LogoutView, MeView, GetCSRFTokenView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='me'),
    path('csrf/', GetCSRFTokenView.as_view(), name='csrf'),
]
