from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContataCurso(forms.Form):

    name = forms.CharField(
        label='Nome',
        max_length=100)

    email = forms.EmailField(
        label='E-mail')

    message = forms.CharField(
        label='Mensagem/Dúvida',
        widget=forms.Textarea)

    def send_mail(self, curso):
        subject = '[%s] Contato' % curso
        message = 'Nome: %(name)s;Email: %(email)s;%(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        message = message % context
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                  [settings.CONTACT_EMAIL])
