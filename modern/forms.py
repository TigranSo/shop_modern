from django import forms
from django.contrib.auth.models import User



class ContactForm(forms.Form):
    phone = forms.CharField(label='Номер телефона', required=True)


class ContactFormMessage(forms.Form):
    from_email = forms.EmailField(label='Почта', required=True)
    subject = forms.CharField(label='Тема', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs = {'cols': 50}), required=True)