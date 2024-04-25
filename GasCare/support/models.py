from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class ServiceRequest(models.Model):
    SERVICE_CHOICES = (
        ('Gas Booking', 'Gas Booking'),
        ('New Connection', 'New Connection'),
        ('Customer Support', 'Customer Support'),
    )

    STATUS_CHOICES = (
        ('resolved', 'Resolved'),
        ('in_progress', 'In Progress'),
    )

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    email = models.EmailField()
    message = models.TextField()
    submission_datetime = models.DateTimeField(auto_now_add=True)
    resolved_datetime = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')

