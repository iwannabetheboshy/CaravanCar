from django import forms
from django.forms import ModelForm, TextInput
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'phone']


        widgets = {
            'first_name': TextInput(attrs={'class': 'contact-field',
                                           'autocomplete': 'off',
                                           'style': 'height: 35px',
                                           'required': True}),

            'phone': TextInput(attrs={'class': 'contact-field',
                                      'type': 'tel',
                                      'pattern': '^[\\d() +-]+$',
                                      'minlength': '6',
                                      'title': 'Пример: 79501234567',
                                      'autocomplete': 'off',
                                      'style': 'height: 35px',
                                      'required': False})
        }
