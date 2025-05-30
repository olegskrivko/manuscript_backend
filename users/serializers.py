from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'role', 'university', 'degree', 'faculty', 'department', 'city', 'country',   'personal_webpage']
