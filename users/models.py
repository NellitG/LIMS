# users/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from laboratories.models import Laboratory

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('tester', 'Tester'),
        ('reviewer', 'Reviewer'),
        ('recommender', 'Recommender'),
        ('issuer', 'Issuer'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    id_number = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    job_role = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    postal_address = models.CharField(max_length=255, blank=True)
    town = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, default='Kenya')

    laboratory = models.ForeignKey(
        Laboratory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

