import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, generics

from questionarios.models.exercicio import Exercicio
from questionarios.models.pessoa import Pessoa
from questionarios.serializer import ExercicioSerializer

class ExerciciosViewSet(viewsets.ModelViewSet):
    
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    http_method_names = ['get']
    
    def retrieve(self, request, pk=None):
        
        json_arr = []
        exercicio = Exercicio.objects.get(pk=pk)
        serializer = ExercicioSerializer(exercicio)
        
        json_arr = serializer.data
        json_arr['pergunta'] = exercicio.pergunta_id.pergunta if exercicio.pergunta_id else None
        json_arr['alternativa_ecolhida'] = exercicio.alternativa_ecolhida_id.resposta if exercicio.alternativa_ecolhida_id else None
        json_arr['usuario'] = exercicio.usuario_id.nome if exercicio.usuario_id else None
        
        return JsonResponse(json_arr)

class DesempenhoViewSet(generics.ListAPIView):
    """ This class generate a json returning the usuario_id, usuario_name and the number of correct answers """
    
    def get(self, request, usuario_id):
        """ This method return a json with the usuario_id, usuario_name and the number of correct answers """
        
        json_arr = []
        json_return = []
        
        # verify if usuario_id exists in database
        try:
            
            aluno = Pessoa.objects.get(pk=usuario_id)
            
            exercicios = Exercicio.objects.filter(usuario_id=usuario_id)
            
            if exercicios.count() > 0:
                
                for exercicio in exercicios:
                    
                    # get all alternativas of the pergunta_id
                    alternativas = exercicio.pergunta_id.alternativa_set.all()
                    
                    alternativa_correta = alternativas.filter(resposta_valida=True)[0]
                    
                    if exercicio.alternativa_ecolhida_id and exercicio.alternativa_ecolhida_id.pergunta_id == exercicio.pergunta_id  and exercicio.alternativa_ecolhida_id.resposta_valida is True:
                    
                        json_arr.append({
                            'aluno_id': exercicio.usuario_id.id,
                            'aluno_name': exercicio.usuario_id.nome,
                            'pergunta': exercicio.pergunta_id.pergunta,
                            'alternativa_ecolhida': exercicio.alternativa_ecolhida_id.resposta,
                            'acertou': True
                        })
                        
                    else:
                        
                        json_arr.append({
                            'aluno_id': exercicio.usuario_id.id,
                            'aluno_name': exercicio.usuario_id.nome,
                            'pergunta': exercicio.pergunta_id.pergunta,
                            'alternativa_ecolhida': exercicio.alternativa_ecolhida_id.resposta if exercicio.alternativa_ecolhida_id else None, 
                            'alternativa_correta': alternativa_correta.resposta,
                            'acertou': False
                        })
                
                total_acertos = 0
                total_erros = 0
                quantidade_questoes = 0
                
                # search in object json_arr the usuario_id and count the number of correct answers
                for json_obj in json_arr:
                    if json_obj['acertou'] is True:
                        total_acertos += 1
                    else :
                        total_erros += 1
                    quantidade_questoes += 1
                
                json_return = {
                    'exercicios': json_arr,
                    'total_acertos': total_acertos,
                    'total_erros': total_erros,
                    'aproveitamento': str((total_acertos / quantidade_questoes) * 100) + '%'
                }
                
                return JsonResponse(json_return, safe=False)
            
            else:
                return JsonResponse({'message': 'Nenhum exercício encontrado para o id de usuário informado'}) 
            
        except Pessoa.DoesNotExist:
            return JsonResponse({'error': 'O aluno informado não existe'})
    
    