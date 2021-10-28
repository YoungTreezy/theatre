from django import forms
from .models import Note
from accounts.models import MyUser


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'finish']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'finish': forms.DateInput(attrs={'class': 'form-control'}),
        }

