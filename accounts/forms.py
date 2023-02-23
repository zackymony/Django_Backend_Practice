from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    birthday = forms.DateField(required=True)
    student_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'birthday', 'student_number']

    def save(self, commit=True):
        user = super(StudentRegistrationForm, self).save(commit=False)
        user.role = 'student'
        user.student_number = self.cleaned_data['student_number']
        if commit:
            user.save()
        return user


class TeacherRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(TeacherRegistrationForm, self).save(commit=False)
        user.role = 'teacher'
        if commit:
            user.save()
        return user
