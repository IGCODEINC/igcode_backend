## Estrutura do Projeto
```bash
├── app/
│   ├── __init__.py           # Arquivo de inicialização do pacote
│   ├── database.py           # Conexão com o MongoDB
│   ├── crud.py               # Funções para manipulação de dados (CRUD)
│   ├── models.py             # Definição dos modelos Pydantic
│   └── main.py               # Arquivo principal com as rotas da API
├── .env                      # Arquivo de configuração de variáveis de ambiente
├── .gitignore                # Arquivo para ignorar arquivos e pastas no Git
├── requirements.txt          # Arquivo com as dependências do projeto
├── README.md                 # Este arquivo (README)
└── run.py                    # Script para rodar a aplicação
```
### Descrição dos Arquivos e Pastas:

- **`app/`**: Diretório que contém todos os arquivos principais da aplicação.
  - **`database.py`**: Arquivo responsável pela conexão com o MongoDB.
  - **`crud.py`**: Contém as funções de manipulação de dados (Create, Read, Update, Delete) do banco de dados.
  - **`models.py`**: Define os modelos de dados usando o Pydantic para validação e estruturação de dados.
  - **`main.py`**: Contém as rotas da API usando o FastAPI.
  
- **`.env`**: Arquivo de configuração das variáveis de ambiente (como chaves de API e configurações de banco de dados).

- **`.gitignore`**: Arquivo para listar arquivos e pastas que devem ser ignorados pelo Git, como dependências e arquivos temporários.

- **`requirements.txt`**: Lista de dependências do projeto, usada para instalar as bibliotecas necessárias com o `pip`.

- **`README.md`**: Este arquivo que descreve o projeto e fornece instruções sobre como configurar e executar a aplicação.

- **`start.py`**: Script para iniciar a aplicação de forma simples, executando o servidor FastAPI.



## Configuração do Ambiente Virtual com Poetry

### Instalação do Poetry (se ainda não instalado):

No terminal, execute:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Instalar as dependências do projeto:

No terminal, execute:
```bash
poetry install
```
### Ativar o ambiente virtual:

No terminal, execute:
```bash
poetry shell
```
## Comando para Rodar o Servidor

Obs. Ja inicia em modo desenvolvimento com reload. 
No diretório do projeto execute:
```bash
poetry run start
```
# Fluxo de Trabalho com Git para Equipe

Ao trabalhar em equipe com Git, é importante seguir uma estratégia de ramificação bem definida para garantir uma colaboração eficiente. Abaixo está um exemplo de fluxo de trabalho utilizando Git.

## 1. Criar uma Branch para Funcionalidades ou Correções de Bugs

Sempre que você começar a trabalhar em uma nova funcionalidade ou correção de bug, crie uma nova branch a partir da branch `main` (ou `develop`). Isso permite que todos trabalhem de forma isolada, sem afetar o código principal de produção.

### Convenção de Nomes de Branches:
- **Branches de Funcionalidades**: `feature/<nome-da-funcionalidade>`
- **Branches de Correções de Bugs**: `bugfix/<nome-do-bug>`
- **Branches de Hotfix**: `hotfix/<nome-do-erro>`

### Exemplo de Criação de Branch para Funcionalidade:

```bash
git checkout -b feature/autenticacao-de-usuario
```
