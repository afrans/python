from django.contrib import admin
from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "idade", "curso", "criado_em")
    search_fields = ("nome", "curso")
    list_filter = ("curso",)
