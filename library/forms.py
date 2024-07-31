from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Library


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['student_name', 'book_name', 'start_date', 'end_date']
        widgets = {
            'student_name': forms.Select(attrs={'class': 'form-control'}),
            'book_name': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Check if start_date is after end_date
        if start_date and end_date and start_date >= end_date:
            raise ValidationError(_("End date should be after start date"))

        return cleaned_data