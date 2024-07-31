from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_class', 'photo', 'video']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_class': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
