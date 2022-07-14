from rest_framework import serializers
from questionarios.models import Pessoa, Alternativa, Exercicio, Pergunta

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ('id', 'pergunta_id', 'alternativa_ecolhida_id', 'usuario_id')