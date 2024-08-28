from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class Usuarios(BaseUserAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined']
    list_display_links = ['username',]
    search_fields = ['username', 'email', 'is_active']
    list_per_page = 10

    fieldsets = (
        (None, {'fields': ('username', 'email')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

class Agendas(admin.ModelAdmin):
    list_display = ['agenda_de', 'nome', 'descricao']
    list_display_links = ['agenda_de', 'nome']
    search_fields = ['agenda_de', 'nome',]
    list_per_page = 10

class Tasks(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'data_inicio', 'data_fim', 'urgencia', 'agenda']
    list_display_links = ['nome',]
    search_fields = ['nome', 'descricao', 'urgencia', 'agenda']
    list_per_page = 10

class Mensagens(admin.ModelAdmin):
    list_display = ['user', 'titulo', 'mensagem', 'data_envio', 'get_task']
    list_display_links = ['user', 'titulo']
    search_fields = ['user', 'titulo', 'get_task']
    list_per_page = 10


admin.site.register(Usuario, Usuarios)
admin.site.register(Agenda, Agendas)
admin.site.register(Task, Tasks)
admin.site.register(Mensagem, Mensagens)