# Monetary API Restful


## Descrição

  

```bash

DESAFIO

Sistema  de  conversão  de  moedas  com  cotações  reais e atuais

A API deve, originalmente, converter entre as seguintes moedas:

USD 
BRL 
EUR 
BTC 
ETH

Ex: USD para BRL, USD para BTC, ETH para BRL, etc...

A requisição deve receber como parâmetros: A moeda de origem, o valor a ser convertido e a moeda final.

Ex: api/currency?from=BTC&to=EUR&amount=123.45

```


## Requisitos
```

-   **Django Rest Framework**: 3.14
-   **Django**: 4.2
-   **Python**: 3.10

```
  

## Instalação

Instalação de todas as dependências do projeto

  

#### Poetry

```bash

  

$  poetry  install

  

```

  

#### Requirements

```bash

  

$  pip  install  -r  requirements.txt

  

```

  

## BD Config

  

#### PostgreSQL

  

```bash

  

# monetary/settings.py

  

.

.

DATABASES  =  {

'default':  {

'ENGINE':  'django.db.backends.postgresql',

'NAME':  os.environ.get('DB_NAME', <db_name>),

'USER':  os.environ.get('DB_USER', <db_user>),

'PASSWORD':  os.environ.get('DB_PASS', <db_password>),

'HOST':  os.environ.get('DB_HOST',  'localhost'),

'PORT':  os.environ.get('DB_PORT', <port>),  #5432

}

}

.

.

```

  

  

## Migração

  

#### Poetry

```bash

  

$  poetry  run  python  manage.py  migrate

  

```

  

#### Python

```bash

  

$  python  manage.py  migrate

  

```

  

  

## Iniciando api

  

#### Poetry

```bash

  

$  poetry  run  python  manage.py  runserver  0.0.0.0:8000

  

```

  

#### Python

```bash

  

$  python  manage.py  runserver  0.0.0.0:8000

  

```

  

# monetary-api