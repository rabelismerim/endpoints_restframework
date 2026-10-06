from django.contrib import admin
from .models import Aluno, Competencia, Mestre, MestreAluno, Reuniao, ReuniaoTarefa

admin.site.site_header = "Administração de mentoria"
admin.site.site_title = "Mentoria API"
admin.site.index_title = "Gestão de mentoria"


@admin.register(Mestre)
class MestreAdmin(admin.ModelAdmin):
    list_display = ("id", "txt_name", "txt_email", "txt_time", "bl_usuario_ativo")
    search_fields = ("txt_name", "txt_email")
    list_filter = ("bl_usuario_ativo", "txt_time")


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("id", "txt_name", "txt_email", "id_mestre", "id_competencia", "bl_usuario_ativo")
    search_fields = ("txt_name", "txt_email")
    list_filter = ("bl_usuario_ativo", "txt_area")
    autocomplete_fields = ("id_mestre", "id_competencia")
    list_select_related = ("id_mestre", "id_competencia")


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("id", "txt_competencia", "txt_tipo", "txt_cargo")
    search_fields = ("txt_competencia", "txt_tipo")


@admin.register(MestreAluno)
class MestreAlunoAdmin(admin.ModelAdmin):
    list_display = ("id", "id_mestre", "id_aluno", "txt_ano_fiscal")
    search_fields = ("id_mestre__txt_name", "id_aluno__txt_name", "txt_ano_fiscal")
    autocomplete_fields = ("id_mestre", "id_aluno")
    list_select_related = ("id_mestre", "id_aluno")


@admin.register(Reuniao)
class ReuniaoAdmin(admin.ModelAdmin):
    list_display = ("id", "txt_comentario", "id_mestre_aluno", "dt_criacao")
    search_fields = ("txt_comentario",)
    autocomplete_fields = ("id_mestre_aluno",)
    list_select_related = ("id_mestre_aluno__id_mestre", "id_mestre_aluno__id_aluno")


@admin.register(ReuniaoTarefa)
class ReuniaoTarefaAdmin(admin.ModelAdmin):
    list_display = ("id", "txt_atividade", "txt_status", "nr_prazo", "dt_conclusao")
    list_filter = ("txt_status",)
    search_fields = ("txt_atividade", "txt_observacao")
    autocomplete_fields = ("id_reuniao", "id_competencia")
