from django.db import models

class Pergunta(models.Model):
    """
        Modelo para perguntas
    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    pergunta = models.TextField(max_length=200)

    def __str__(self):
        return self.pergunta