from django.db import models

class Pessoa(models.Model):
    """
        Modelo para pessoas
    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome