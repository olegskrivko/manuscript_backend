from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser  # instead of AbstractBaseUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):  # inherit from AbstractUser to get username by default
    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=[
            ('author', 'Author'),
            ('reviewer', 'Reviewer'),
            ('editor', 'Editor'),
            ('admin', 'Admin'),
        ],
        default='author',
    )
    degree = models.CharField(max_length=100, blank=True)
    faculty = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    university = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    personal_webpage = models.URLField(blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.username} - {self.email}"

