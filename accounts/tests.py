from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    STUDENT = 'student'
    TEACHER = 'teacher'
    SYSTEM_ADMIN = 'system_admin'
    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (SYSTEM_ADMIN, 'System Admin'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    birthday = models.DateField(null=True, blank=True)
    student_number = models.CharField(max_length=50, null=True, blank=True)
    class_name = models.CharField(max_length=50, null=True, blank=True)
    teacher = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
