from django.contrib import admin
from .models import Curso, Inscricao, Anuncio, Comentario


class CursoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Curso, CursoAdmin)
admin.site.register([Inscricao, Anuncio, Comentario])
