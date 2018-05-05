from django import forms


class ContataCurso(forms.Form):

	name = forms.CharField(
		label='Nome',
		max_length=100)

	email = forms.EmailField(
		label='E-mail')

	message = forms.CharField(
		label='Mensagem/Dúvida',
		widget=forms.Textarea)
