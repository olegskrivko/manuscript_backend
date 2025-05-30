from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
import random

User = get_user_model()

# List all users (public)
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Retrieve individual user details (public)
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Update user (public for demo purposes)
class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUserView(APIView):
    def get(self, request):
        users = User.objects.all()
        if users.exists():
            random_user = random.choice(users)
            serializer = UserSerializer(random_user)
            return Response(serializer.data)
        else:
            # fallback demo user if database is empty
            demo_user = {
                "id": 0,
                "username": "demo_user",
                "email": "demo@example.com",
                "role": "author",
                "degree": "PhD",
                "faculty": "Demo Faculty",
                "department": "Demo Department",
                "university": "Demo University",
                "city": "Demo City",
                "country": "Demo Country",
                "personal_webpage": "https://example.com",
                "is_verified": True,
                "first_name": "Demo",
                "last_name": "User",
            }
            return Response(demo_user)
