
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    birthday = forms.DateField(required=True)
    student_number = forms.CharField(required=True)
    role = forms.ChoiceField(choices=[('teacher', 'Teacher'), ('student', 'Student')], widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'birthday', 'student_number', 'role']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.role = self.cleaned_data['role']
        user.student_number = self.cleaned_data.get('student_number', '')
        if commit:
            user.save()
        return user

