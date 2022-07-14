from django.db import models
from questionarios.models.alternativa import Alternativa

from questionarios.models.pergunta import Pergunta
from questionarios.models.pessoa import Pessoa

class Exercicio(models.Model):
    pergunta_id = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True, blank=True)
    alternativa_ecolhida_id = models.ForeignKey(Alternativa, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.pergunta_id.pergunta
