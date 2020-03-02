from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Localizacao


@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    """
    Cadastro do model Localizacao no painel administrativo do django.
    Sem essa classe não é possível manipular os dados pelo django admin.
    """
    list_display = ['nome', 'pos_x', 'pos_y', 'hor_abertura', 'hor_fechamento', 'modified', 'created']
    list_filter = ['nome']
    search_fields = ['id', 'unique_id', 'nome', 'pos_x', 'pos_y', 'hor_abertura', 'hor_fechamento', 'modified', 'created']
    ordering = ['modified', 'id']
