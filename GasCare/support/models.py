from django.db import models
from  django.contrib.auth.models import User
import datetime
# Create your models here.


class ServiceRequest(models.Model):
    SERVICE_CHOICES = (
        ('Gas Booking', 'Gas Booking'),
        ('New Connection', 'New Connection'),
        ('Customer Support', 'Customer Support'),
    )

    STATUS_CHOICES = (
        ('Resolved', 'Resolved'),
        ('In Progress', 'In Progress'),
    )

    user_id=models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column="userid")
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    email = models.EmailField()
    message = models.TextField()
    submission_datetime = models.DateTimeField(auto_now_add=True)
    resolved_datetime = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    def __str__(self):
        return f"Service Request {self.pk} - User:{self.user_id.username}"

