from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author', 'publication', 'year']
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publication': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
