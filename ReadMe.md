Olá este código foi desenvolvido em Python com o objetivo de demonstrar alguns de meus conhecimentos em Python.

# Como faço para rodar o código?

* Primeiro, você deve se certificar de ter docker instalado no seu computador.
* Depois, você deve abrir o terminal e clonar este repo e entrar nele
* Na pasta do repo realizar o build do docker com o comando:
    
    - docker-compose build

* Depois, você deve realizar as migrations do banco de dados e gerar os arquivos staticos com o comando:
    
    - docker-compose run web python manage.py migrate

    - docker-compose run web python manage.py collectstatic

* !Observação não esqueça de criar o superuser atráves do comando:
    
    - docker-compose run web python manage.py createsuperuser 

* Depois, você deve rodar o servidor do docker com o comando:
    
    - docker-compose up

* Para acessar o admin entre em http://localhost:8000/admin/ e faça o login com o usuário admin e senha admin, lá dentro realize as operações que desejar.

* Depois, você deve acessar o site:
    http://localhost:8000/

# ABOUT PROJECT

    Neste projeto a na sua rota padrão possui a interface do djangorestframework da qual pode fornecer informações sobre os exercicios de forma resumida.

    Na rota 'exercicios/["id_exercicio"]' você pode ver os detalhes do exercicio informado.

    O desempenho de cada aluno está em 'desempenho/["id_aluno"]'.


