from django.db import models


class Cursos(models.Model):

	name = models.CharField(
		verbose_name='Nome',
		max_length=100)

	slug = models.SlugField(
		verbose_name='Atalho')

	description = models.TextField(
		verbose_name='Descrição',
		blank=True)

	start_date = models.DateField(
		verbose_name='Data de inicio',
		null=True,
		blank=True)

	image = models.ImageField(
		upload_to='cursos/images',
		verbose_name='Imagem',
		null=True,
		blank=True)

	created_at = models.DateTimeField(
		verbose_name='Criado em',
		auto_now_add=True)

	updated_at = models.DateTimeField(
		verbose_name='Atualizado em',
		auto_now=True)