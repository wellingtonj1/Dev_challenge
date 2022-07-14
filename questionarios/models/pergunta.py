from django.db import models

class Pergunta(models.Model):
    pergunta = models.TextField(max_length=200)

    def __str__(self):
        return self.pergunta