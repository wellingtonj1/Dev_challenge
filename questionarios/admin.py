from django.contrib import admin
from django import forms

from questionarios.models.alternativa import Alternativa
from questionarios.models.exercicio import Exercicio
from questionarios.models.pergunta import Pergunta
from questionarios.models.pessoa import Pessoa

class Exercicios(admin.ModelAdmin):
    
    #show question text instead of id
    def pergunta(self, obj):
        return obj.pergunta_id.pergunta
    
    # show answer text instead of id
    def alternativa(self, obj):
        # verify if has an answer
        if obj.alternativa_ecolhida_id:
            return obj.alternativa_ecolhida_id.resposta
        return "--"
    
    # show if alternativa is valid
    def alternativa_valida(self, obj):
        # verify if has an answer
        if obj.alternativa_ecolhida_id:
            if obj.alternativa_ecolhida_id.resposta_valida and obj.pergunta_id == obj.alternativa_ecolhida_id.pergunta_id:
                return "Sim"
            return "Não"
        return "--"
    
    # show user name instead of id
    def usuario(self, obj):
        if obj.usuario_id:
            return obj.usuario_id.nome
        return "--"
    
    list_display = ('pergunta', 'alternativa', 'alternativa_valida', 'usuario')
    list_display_links = ('pergunta', 'alternativa', 'alternativa_valida', 'usuario')  
    list_per_page = 10
    
class Alternativas(admin.ModelAdmin):
    
    # show question text instead of id
    def pergunta(self, obj):
        return obj.pergunta_id.pergunta
    
    # show answer text instead of id
    def alternativa(self, obj):
        return obj.resposta
    
    # show if alternativa is valid
    def alternativa_valida(self, obj):
        if obj.resposta_valida:
            return "Sim"
        return "Não"
    
    list_display = ('pergunta', 'alternativa', 'alternativa_valida')
    list_display_links = ('pergunta', 'alternativa')
    search_fields = ('pergunta', 'alternativa')
    list_per_page = 10

class Perguntas(admin.ModelAdmin):
        
    # show question text instead of id
    def pergunta(self, obj):
        return obj.pergunta
    
    list_display = ('pergunta',)
    list_display_links = ('pergunta',)
    search_fields = ('pergunta',)
    list_per_page = 10

class Pessoas(admin.ModelAdmin):
        
    # show user name instead of id
    def nome(self, obj):
        return obj.nome
    
    list_display = ('nome',)
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Exercicio, Exercicios)
admin.site.register(Alternativa, Alternativas)
admin.site.register(Pergunta, Perguntas)
admin.site.register(Pessoa, Pessoas)
# admin.site.register(Exercicio, Exercicios)