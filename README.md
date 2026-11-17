#Projeto Revenda de Carros

Aplicação web desenvolvida com **Python e Django**, simulando o funcionamento de uma plataforma de revenda de veículos.

O projeto tem como objetivo praticar conceitos de desenvolvimento web, organização de aplicações Django, autenticação de usuários e integração com banco de dados.

## Tecnologias utilizadas

- **Python** – Linguagem principal.
- **Django 6.0** – Framework para desenvolvimento web.
- **PostgreSQL** – Banco de dados relacional.
- **Pillow** – Processamento de imagens.
- **HTML e CSS** – Estruturação e estilização das páginas.

## Funcionalidades

- Cadastro de veículos.
- Listagem de veículos disponíveis.
- Sistema básico de autenticação de usuários.
- Integração com banco de dados.
- Organização do projeto em aplicações independentes.

## Estrutura do projeto

```text
Projeto-Revenda-Carros/
│
├── accounts/       # Aplicação relacionada aos usuários
├── app/            # Aplicação principal
├── cars/           # Gerenciamento de veículos
│
├── manage.py
├── requirements.txt
└── .gitignore
```

## Como executar o projeto

**1. Clone o repositório**

```bash
git clone https://github.com/Kaue-Oliveira-Freitas/Projeto-Revenda-Carros.git
```

**2. Acesse a pasta**

```bash
cd Projeto-Revenda-Carros
```

**3. Crie um ambiente virtual**

```bash
python -m venv venv
```

**4. Ative o ambiente virtual**

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

**5. Instale as dependências**

```bash
pip install -r requirements.txt
```

**6. Configure o banco de dados**

Configure as credenciais e a conexão com o banco de dados conforme as configurações do projeto.

**7. Execute as migrações**

```bash
python manage.py migrate
```

**8. Inicie o servidor**

```bash
python manage.py runserver
```

Acesse a aplicação pelo navegador:

```text
http://127.0.0.1:8000/
```

## 📚 Objetivo do projeto

Este projeto foi desenvolvido como parte da minha jornada de aprendizado em Ciência da Computação, com foco na aplicação prática de conceitos de programação e desenvolvimento web utilizando Django.

Através dele, busquei aprimorar meus conhecimentos em Python, desenvolvimento back-end, estruturação de aplicações e gerenciamento de bancos de dados.

## 👨‍💻 Desenvolvedor

**Kauê Oliveira Freitas**

Estudante de Ciência da Computação e desenvolvedor em formação, interessado em desenvolvimento web, Python e tecnologias back-end.

[GitHub](https://github.com/Kaue-Oliveira-Freitas)
