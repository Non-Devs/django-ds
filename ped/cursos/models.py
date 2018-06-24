from django.db import models
from django.urls import reverse
from django.conf import settings
from ped.core.mail import send_mail_template

class GerenciaCurso(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query))


class Curso(models.Model):
    name = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    slug = models.SlugField(
        verbose_name='Atalho'
    )

    description = models.TextField(
        verbose_name='Descrição simples',
        blank=True
    )

    about = models.TextField(
        verbose_name='Sobre o curso',
        blank=True)

    start_date = models.DateField(
        verbose_name='Data de inicio',
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to='cursos/images',
        verbose_name='Imagem',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Atualizado em',
        auto_now=True
    )

    objects = GerenciaCurso()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cursos:details', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']


class Lição(models.Model):

    name = models.CharField("Nome", max_length=100)

    description = models.TextField('Descrição', blank=True)

    number = models.IntegerField('Números(ordem)', blank=True, default=0)

    release_date = models.DateField('Data de liberação', blank=True, null=True)

    curso = models.ForeignKey(Curso, verbose_name='Curso', related_name='Lições', on_delete='CASCADE')

    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['number']


class Material(models.Model):

    name = models.CharField("Nome", max_length=100)

    embedded = models.TextField('Video embedded', blank=True)

    file = models.FileField(upload_to='licoes/materiais', blank=True, null=True)

    licao = models.ForeignKey(Lição, verbose_name='aula', related_name='materials', on_delete='CASCADE')

    def is_embedded(self):
        return bool(self.embedded)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'


class Inscricao(models.Model):

    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        related_name='inscricao',
        on_delete='CASCADE'
    )

    curso = models.ForeignKey(
        Curso,
        verbose_name='Curso',
        related_name='inscricao',
        on_delete='CASCADE'
    )

    status = models.IntegerField(
        'Situação',
        choices=STATUS_CHOICES,
        default=0,
        blank=True
    )

    created_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Atualizado em',
        auto_now=True
    )

    def active(self):
        self.status = 1
        self.save()

    def is_approved(self):
        return self.status == 1

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'curso'),)


class Anuncio(models.Model):

    cursos = models.ForeignKey(Curso, verbose_name='Curso',related_name='anuncios', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    conteudo = models.TextField('Conteudo')

    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'
        ordering = ['-created_at']


class Comentario(models.Model):
    anuncio = models.ForeignKey(Anuncio, verbose_name = 'Anúncio', related_name='comentarios', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='usuário', on_delete=models.CASCADE)
    comentario = models.TextField('Comentário')

    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['-created_at']


def post_save_anuncio(instance, created, **kwargs):
    if created:
        subject = instance.titulo
        context = {
            'anuncio': instance,
        }
        template_name = 'cursos/anuncios_email.html'
        inscricoes = Inscricao.objects.filter(
            curso=instance.cursos,
            status=1
        )
        for inscricao in inscricoes:
            recipient_list = [inscricao.user.email]
            send_mail_template(subject, template_name, context, recipient_list)


models.signals.post_save.connect(
    post_save_anuncio,
    sender=Anuncio,
    dispatch_uid='post_sabe_anuncio'
)





