# Flix App

Flix App é um frontend desenvolvido em Streamlit que consome dados de uma API criada com Django Rest Framework. Este projeto permite que os usuários visualizem informações de filmes, gêneros, atores e avaliações, com funcionalidades de autenticação para acessar e gerenciar conteúdo personalizado.

## Funcionalidades

- **Login e Autenticação**: Interface para login e gerenciamento de sessão.
- **Visualização de Filmes**: Lista de filmes com detalhes específicos, como título, sinopse, gênero e elenco.
- **Avaliações de Filmes**: Permite que os usuários visualizem e interajam com avaliações de filmes.
- **Catálogo de Gêneros e Atores**: Navegação por categorias e informações dos atores.
- **Consumo de API**: Integração com uma API desenvolvida em Django Rest Framework para obtenção e envio de dados.

## Estrutura do Projeto

```plaintext
FLIX_APP/
├── actors/            # Interface de navegação para os atores
├── api/               # Configuração de integração com a API
├── genres/            # Exibição de gêneros disponíveis
├── home/              # Página inicial do aplicativo
├── login/             # Autenticação e login de usuário
├── movies/            # Exibição de filmes com detalhes
├── reviews/           # Sessão de avaliações dos filmes
├── venv/              # Ambiente virtual para dependências do projeto
├── .flake8            # Configuração do Flake8 para estilo de código
├── .gitignore         # Arquivo Gitignore
├── app.py             # Arquivo principal para execução do Streamlit
├── config.toml        # Configurações do Streamlit
└── requirements.txt   # Dependências do projeto
```

## Pré-requisitos

- **Python 3.8+**
- **Django Rest Framework** (para a API backend)
- **Streamlit** (para o frontend)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/PedroTomasini/flix_app.git
   cd flix-app
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Para Linux e macOS
   venv\Scripts\activate     # Para Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Configuração

- **API Backend**: Certifique-se de que a API em Django Rest Framework esteja em execução e acessível.
- **Configuração do Streamlit**: Verifique o arquivo `config.toml` para ajustes de configurações.

## Executando o Aplicativo

Com o ambiente virtual ativado, inicie o Streamlit:

```bash
streamlit run app.py
```

Abra o navegador e acesse `http://localhost:8501` para visualizar o aplicativo.

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests para melhorias e novas funcionalidades.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

Esse README proporciona uma visão geral das funcionalidades do projeto, instruções de configuração e como executá-lo localmente.
