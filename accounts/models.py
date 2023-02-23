
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('sys_admin', 'System Admin'),
    )
    user_role = models.CharField(max_length=200, choices=USER_ROLES, default='student')
    student_number = models.CharField(max_length=20, null=True, blank=True)

class Class(models.Model):
    class_name = models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birthday = models.DateField()
    student_number = models.CharField(max_length=20)
    email = models.EmailField()
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='students')

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()

