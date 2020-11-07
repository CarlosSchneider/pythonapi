

# Python API REST Example

Um simples exemplo de api rest com python

# Primeira versão

lista de estudantes

## endpoints disponiveis 
* GET UTF8 ${[http/https]://localhost}/5005/info   = mostra o arquivo README.md
* GET UTF8 ${[http/https]://localhost}/5005/info.html   = mostra o arquivo README.md em html

* GET UTF8 ${[http/https]://localhost}/5005/load   = mostra toda a lista de estudantes
* GET UTF8 ${[http/https]://localhost}/5005/info/${id}   = mostra o dados de um estudante especifico
* GET UTF8 ${[http/https]://localhost}/5005/info/?name=${valor}   = mostra a lista dos estudantes que tem valor no nome

* POST UTF8 ${[http/https]://localhost}/5005/isvalid  = valida um json como cumprindo as regras do negocio para o registro

* POST UTF8 ${[http/https]://localhost}/5005/insert  = insere um novo registro com os dados do json

* PUP UTF8 ${[http/https]://localhost}/5005/update  = altera um novo registro com os dados do json

* PUP UTF8 ${[http/https]://localhost}/5005//delete/${id} = exclui um registro
  - Obs.: requer uma chave para validar a operacao { data='{"key": ${id * 3}}' }


## modelo do json 
  {
    "id": int ou nulo,
    "name": string entre 5 e 60 caracteres,
    "email": e-mail valido nao vazio,
    "gender": string ou nulo
  }, 


## Disponivel em 

[GITHUB][https://github.com/CarlosSchneider/pythonapi]


