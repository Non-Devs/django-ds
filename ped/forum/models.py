from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


class Thread(models.Model):

    title = models.CharField('Título', max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Autor',
        related_name='threads',
        on_delete='CASCADE'
    )
    body = models.TextField('Mensagem')
    views = models.IntegerField('Visualizações', blank=True, default=0)
    answers = models.IntegerField('Respostas', blank=True, default=0)
    tags = TaggableManager()

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Criado em', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Topico'
        verbose_name_plural = 'Tópicos'
        ordering = ['-modified']


class Reply(models.Model):

    reply = models.TextField('Resposta')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Autor',
        related_name='replies',
        on_delete='CASCADE'
    )
    correct = models.BooleanField('Correta?', blank=True, default=False)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Criado em', auto_now=True)

    def __str__(self):
        return self.reply[:100]

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        ordering = ['-correct','created']