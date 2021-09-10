# Projeto Universo NextLevel

Universo NextLevel é um projeto de sistema Web com Python e Django para
Gerenciamento de conteúdo de um universo de RPG de Mesa, como, por exemplo,
personagens não jogáveis (NPC).

Desenvolvido em Live na Twitch

https://twitch.tv/leonextlevel


# Executando o projeto

### Requisitos
* Python 3.9

### Criar ambiente virtual
```bash
python -m venv .venv --prompt universo-nextlevel
```

### Ativar o ambiente virtual
No Linux e Mac
```bash
source /path/to/venv/bin/activate
```
No Windows usando CMD
```bash
path\to\venv\Scripts\activate.bat
```
No Windows usando PowerShell
```bash
path\to\venv\Scripts\activate.bat
```

### Instalar as dependências

1 vez
```bash
pip install -r requirements-dev.txt
```

outras vezes
```bash
pip-sync requirements-dev.txt
```

### Aplicar as migrações
```bash
python manage.py migrate
```

### Executar o projeto
```bash
python manage.py runserver
```

### Atualizar as dependências

```bash
pip-compile --generate-hashes requirements.in

pip-compile --generate-hashes requirements-dev.in
```

## Se gostou deixe uma ⭐ e vá conhecer meu trabalho na Twitch ❤️
