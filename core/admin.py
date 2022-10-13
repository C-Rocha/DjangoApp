from django.contrib import admin

from .models import Cargo, Funcionario, Servico, Features, Planos, Cliente

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['cargo', 'criados', 'modificado', 'ativo']

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['servico', 'descricao', 'icone', 'criados', 'modificado', 'ativo']

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'bio', 'imagem','facebook' , 'twitter', 'instagram', 'criados', 'modificado', 'ativo']

@admin.register(Features)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'icone','criados', 'modificado', 'ativo']

@admin.register(Planos)
class PlanosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'preco', 'icone','criados', 'modificado', 'ativo']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'profissao', 'descricao', 'avaliacao','imagem','criados', 'modificado', 'ativo']
