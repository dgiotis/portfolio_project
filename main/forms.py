from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-lg bg-gray-800 text-white border border-gray-700',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-3 rounded-lg bg-gray-800 text-white border border-gray-700',
                'placeholder': 'Your email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-lg bg-gray-800 text-white border border-gray-700',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full p-3 rounded-lg bg-gray-800 text-white border border-gray-700 h-32',
                'placeholder': 'Your message'
            }),
        }
