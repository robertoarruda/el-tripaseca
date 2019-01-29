# El Tripaseca

## Pré-requisitos
- Python 3 `sudo apt-get install python3`
- Pip `sudo apt-get install python3-pip`
- VirtualEnv `sudo pip3 install virtualenv`


## Instalação

### Clone o projeto:
```
git clone git@github.com:robertoarruda/el-tripaseca.git
```

### Crie o ambiente:
Dentro da raiz do projeto, execute o comando abaixo:
```
virtualenv venv --python=python3
```

### Ative o ambiente:
Execute o comando abaixo para ativar:
```
source venv/bin/activate
```

### Instale as dependencias:
Execute o comando abaixo para instalar as dependencias do projeto:
```
pip install -r requirements.txt
```

### Edite os dados de login
Insira o usuário e senha do perfil usado para consulta
```
#main.py

login = '****@****.com'
password = '******'
```

### Execute o script:
Execute o comando abaixo para rodar o script:
```
python main.py
```

### Acesse o app local
http://localhost:5000/profile/robertoadearruda


### Desative o ambiente:
Execute o comando abaixo para desativar:
```
deactivate
```