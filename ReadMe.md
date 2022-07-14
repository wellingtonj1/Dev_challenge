Olá este código foi desenvolvido em Python com o objetivo de demonstrar alguns de meus conhecimentos em Python.

Como faço para rodar o código?

    - Primeiro, você deve se certificar de ter o Python instalado no seu computador.
    - Depois, você deve abrir o terminal e clonar este repo e entrar nele
    - Na pasta do repo realizar o build do docker com o comando:
        docker-compose build
    - Depois, você deve realizar as migrations do banco de dados e gerar os arquivos staticos com o comando:
        docker-compose run web python manage.py migrate

    - Depois, você deve rodar o servidor do docker com o comando:
        docker-compose up
    - Depois, você deve acessar o site:
        http://localhost:8000/

        
    

