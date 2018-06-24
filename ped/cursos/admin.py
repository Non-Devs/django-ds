from django.contrib import admin
from .models import Curso, Inscricao, Anuncio, Comentario, Lição, Material


class CursoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class MaterialInlineAdmin(admin.TabularInline):

    model = Material


class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'curso', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at']
    inlines = [MaterialInlineAdmin]


admin.site.register(Curso, CursoAdmin)
admin.site.register([Inscricao, Anuncio, Comentario])
admin.site.register(Lição, LessonAdmin)
