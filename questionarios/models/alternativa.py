from django.db import models

from questionarios.models.pergunta import Pergunta

class Alternativa(models.Model):
    """
        Modelo para alternativas
    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    resposta = models.TextField(max_length=200)
    pergunta_id = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta_valida = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.pergunta_id) + " -- R: " + self.resposta