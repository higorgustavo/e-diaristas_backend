# Projeto e-diaristas

### Instalando o projeto

#### Clonar o projeto
`get clone https://github.com/higorgustavo/e-diaristas_backend`

#### Instalar dependências
`pip install -r requirements.txt`

#### Aletrar configurações do Banco de Dados no `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_bd',
        'HOST': 'host_do_bd',
        'PORT': 'porta_bd',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'
    }
}
```

#### Migrar Banco de Dados
`python manage.py migrate`

#### Iniciar servidor
`python manage.py runserver`