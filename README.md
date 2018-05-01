# PED: Plataforma de ensino a distância

![logo](https://user-images.githubusercontent.com/14116020/38166532-77b3097a-34fb-11e8-9b17-fb06082d6fb3.png)

O projeto se trata de uma plataforma de ensino a distância, na qual terá como funcionalidades um sistema de autenticação, forum de discussão e cursos online.

### Membros:

|Nome|Função|
|----|------|
|João Sconetto|Devops e Gerência|
|Victor Arnaud|Devops e Arquitetura|
|Júlia Pessoa|Documentação|
|Heron|Desenvolvimento|
|Elias Bernardo|Desenvolvimento|

### Iniciando o projeto: 


Primeiramente clone o repositório:

  `cd ~/Documentos`
  
 `mkdir "diretório"`

 `cd "diretório"`

 `git clone https://github.com/Non-Devs/django-ds.git`

Agora, considerando que você possui o Python instalado:

`sudo apt-get install python3-venv` 

`python3 -m venv venv`

`cd venv`

`source bin/activate`

Dentro da VirtualEnv:

`python -m pip install django`

`python -m pip install Pillow`

`cd .. && cd django-ds/`

`python manage.py migrate`

`python manage.py runserver`

